from ai_model import model
from data import write_json

def chat(prompt):
    text = "あなたは私の彼女です。私と会話してください。絵文字とかも使ってほしいです。"

    # 会話履歴を読み込み、ユーザーのプロンプトを追加
    try:
        messages = write_json.read_from_json()
    except:
        messages = [{"role": "user", "content": text}]
    messages.append({"role": "user", "content": prompt})
    response = model.reply(messages)
    return response