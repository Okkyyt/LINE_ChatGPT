from openai import OpenAI
from data import write_json

client = OpenAI()

def reply(messages,userId):
    # OpenAIのAPIを呼び出し、与えられたメッセージに対する応答を取得
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    response = completion.choices[0].message.content
    # 応答を保存
    new_message={'role':'assistant', 'content':response}
    messages.append(new_message)
    print(messages)
    write_json.write_to_json(messages,userId)
    return response