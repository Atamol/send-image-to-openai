import base64
from openai import OpenAI

# OpenAI API Key
client = OpenAI(api_key="your_api_key")

# ローカルの画像ファイルパス
image_path = r"your_image_path"

# 画像をBase64エンコード
with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# data URLの形式に変換
data_url = f"data:image/jpeg;base64,{encoded_string}"

# APIの呼び出し
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
                        "url": data_url,
                    },
                },
            ],
        }
    ],
    max_tokens=1500,
)

# 応答内容の表示
print("Assistant:", response.choices[0].message.content)

# トークン消費量の表示
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
