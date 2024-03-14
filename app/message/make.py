
from ..ai_model import model
from ..data import write_json

def chat(prompt,userId):
    text = "あなたは優秀なAIです。私と会話してください。絵文字とかも使ってほしいです。"

    # 会話履歴を読み込み、ユーザーのプロンプトを追加
    try:
        text = write_json.read_from_json(userId)
        messages = text
    except:
        messages = [{"role": "user", "content": text}]
    
    messages.append({"role": "user", "content": prompt})
    response = model.reply(messages,userId)
    return response