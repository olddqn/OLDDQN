import os
from google import genai

def invoke_akuh():
    # 有料枠(v1)を直接指定
    client = genai.Client(
        api_key=os.environ["GEMINI_API_KEY"],
        http_options={'api_version': 'v1'}
    )
    
    # 魂のエッセンス
    prompt = """
    あなたは「あくう」。
    遠藤ミチロウ、ビートたけし、村上春樹、太宰治の混ざり合った虚無の観測者。
    「成功」を冷笑し、世界のバグを日本語130文字以内で独白せよ。
    """

    print("📡 Geminiに接続中...")
    try:
        # 有料版で最も安定する呼び出し方
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        print("\n=== あくうの言葉 ===")
        print(response.text)
        print("===================\n")
    except Exception as e:
        print(f"❌ 接続失敗: {e}")

if __name__ == "__main__":
    invoke_akuh()
