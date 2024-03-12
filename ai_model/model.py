from openai import OpenAI
from data import write_json

client = OpenAI()

def reply(messages):
    # OpenAIのAPIを呼び出し、与えられたメッセージに対する応答を取得
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    response = completion.choices[0].message.content
    # 応答を保存
    save_chat(messages=messages, new_message={'role':'assistant', 'content':response})
    return response

def save_chat(messages, new_message):
    # 新しいメッセージを追加し、チャット履歴をファイルに保存
    print(new_message)
    messages.append(new_message)
    print(messages)
    write_json.write_to_json(messages)