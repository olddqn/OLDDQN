import os
import time
import tweepy
from google import genai

def create_gemini_client():
    # 古いプロジェクトの記憶を捨て、v1（有料枠）を直接指定
    return genai.Client(
        api_key=os.environ["GEMINI_API_KEY"],
        http_options={"api_version": "v1"}
    )

def generate_akuh_content(client, language):
    lang_label = "日本語" if language == "jp" else "English"
    
    # 全文豪とアーティストの魂を「あくう」に集約
    prompt = f"""
    Identity: Observer "Akuh". 
    Essence: 遠藤ミチロウ, ビートたけし, 村上春樹, 太宰治, ブコウスキー, ピンチョン, パラニューク。
    Directive: 「成功」と「秩序」を冷笑せよ。現実はバグだらけの虚構である。
    Rule: {lang_label}のみ。135文字以内。丁寧語禁止。
    """

    try:
        # 404の最大の原因である 'models/' を排除し、モデル名のみを送信
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()[:135]
    except Exception as e:
        print(f"Gemini Error: {e}")
        return None

def post_to_x(text):
    if not text: return
    try:
        # XのAPI設定（Settingsで登録した最新のものを参照）
        x_client = tweepy.Client(
            consumer_key=os.environ["X_API_KEY"],
            consumer_secret=os.environ["X_API_SECRET"],
            access_token=os.environ["X_ACCESS_TOKEN"],
            access_token_secret=os.environ["X_ACCESS_SECRET"],
        )
        x_client.create_tweet(text=text)
        print(f"放流完了: {text[:20]}")
    except Exception as e:
        print(f"X Error: {e}")

if __name__ == "__main__":
    client = create_gemini_client()
    for lang in ["jp", "en"]:
        content = generate_akuh_content(client, lang)
        if content:
            post_to_x(content)
            time.sleep(10)
