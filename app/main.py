from dotenv import load_dotenv
from fastapi import FastAPI, BackgroundTasks, Request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent,QuickReply,TextSendMessage
import json
import os

from .message import make
from .data import write_json

app = FastAPI()
ans = False
# ApiRoot Health Check
@app.get("/")
def api_root():
    return {"message": "LINEBOT-API-Healthy"}

load_dotenv()

# LINE Messaging APIの準備
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET = os.getenv("CHANNEL_SECRET")

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.post("/")
async def callback(request:Request,background_tasks:BackgroundTasks):
    body = await request.body()
    data_json = json.loads(body)
    background_tasks.add_task(handle_message,data_json)
    #INFO:     147.92.150.193:0 - "POST / HTTP/1.1" 200 OK
    #'{"destination":"U94530c9340e4fe7045c73b0450a86980","events":[{"type":"message","message":{"type":"text","id":"498465752207065399","quoteToken":"NWEg2cuIKkGODtObK5YL2QL9Wzmws-kDYj2uaNvijNxWI2vy14zHX81qEGGJV9cEISHUB98TS3J02J1rBMCWyJRSvTRbUaam8CZ8M-6SLIagRdg74EQqq7Cf9DbUNF1_XtD1opq0xnUBVkrIwLYnPQ","text":"hello"},"webhookEventId":"01HRG5WXPRTKEDGEPCKG680NXS","deliveryContext":{"isRedelivery":false},"timestamp":1709940045104,"source":{"type":"user","userId":"Ufb88bea97c59e74464a5666598703157"},"replyToken":"16222b97f3ea474e8b062c0d6028c2ac","mode":"active"}]}'
    return data_json

# LINE Messaging APIからのメッセージイベントを処理
@handler.add(MessageEvent)
def handle_message(data_json):
    global ans
    replyToken = data_json["events"][0]["replyToken"]
    message = data_json["events"][0]["message"]["text"]

    label = 'チャットを終える'
    
    quick_text = QuickReply(
        items=[
            {
                'type': 'action',
                'action': {
                    'type': 'message',
                    'label': label,
                    'text': label,  
                },
            },
        ]
    )

    userId = data_json["events"][0]["source"]["userId"]
    if message == label:
        write_json.delete_json(userId)
        return
    else :
        ans =  True
     
    res = make.chat(message,userId)
    res_message = TextSendMessage(text=res, quick_reply=quick_text)
    line_bot_api.reply_message(reply_token=replyToken,messages=res_message)