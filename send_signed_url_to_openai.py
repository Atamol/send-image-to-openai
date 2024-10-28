from openai import OpenAI

# OpenAI API Key
client = OpenAI(api_key = "your_api_key")

# API 呼び出し
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "画像が何を表しているか説明してください。"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://s3.amazonaws.com/test.jpg?AWSAccessKeyId=test&Signature=test&Expires=114514",
                    },
                },
            ],
        }
    ],
    max_tokens=2000,
)

print("Assistant:", response.choices[0].message.content)

# Token消費量の表示
try:
    usage = response.usage
    prompt_tokens = usage.prompt_tokens
    completion_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens

    print(f"Prompt Tokens: {prompt_tokens}")
    print(f"Completion Tokens: {completion_tokens}")
    print(f"Total Tokens: {total_tokens}")
except AttributeError:
    print("Usage情報がレスポンスに含まれていません。")
