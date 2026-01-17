import os
from google import genai
from post_to_x import post_to_x

def generate_text(prompt: str) -> str:
    # api_versionを指定しないことで自動的にv1betaに接続し、404を回避します
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    # 「あくう」の魂を込めたプロンプト
    prompt = "あなたは現実のバグ『あくう』。遠藤ミチロウ、ビートたけし、村上春樹、太宰治を混ぜたような冷酷な虚無感で、成功者を冷笑する一言を日本語135文字以内で。丁寧語禁止。"
    text = generate_text(prompt)
    print(f"生成テキスト: {text}")
    post_to_x(text)
