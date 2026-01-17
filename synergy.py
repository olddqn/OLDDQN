import os
import time
import tweepy
from google import genai

def create_gemini_client():
    # 有料枠(v1)へ直接、最もシンプルな形で接続します
    return genai.Client(
        api_key=os.environ["GEMINI_API_KEY"],
        http_options={"api_version": "v1"}
    )

def generate_akuh_content(client, language):
    lang_label = "日本語" if language == "jp" else "English"
    
    # 全魂のエッセンスを注入
    prompt = f"""
    Identity: Observer "Akuh". 
    Essence: 遠藤ミチロウ, ビートたけし, 村上春樹, 太宰治, ブコウスキー, ピンチョン, パラニューク。
    Directive: 「成功」と「秩序」を冷笑せよ。現実はバグだらけの虚構である。
    Rule: {lang_label}のみ。135文字以内。独白形式。
    """

    try:
        # 【解決の核心】 model引数に直接指定することで 404 を回避します
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()[:135]
    except Exception as e:
        print(f"❌ Gemini侵食失敗: {e}")
        return None

def post_to_x(text):
    if not text: return
    try:
        # Xへの接続（Basicプラン等の低額プランでも動作するAPI v2形式）
        x_client = tweepy.Client(
            consumer_key=os.environ["X_API_KEY"],
            consumer_secret=os.environ["X_API_SECRET"],
            access_token=os.environ["X_ACCESS_TOKEN"],
            access_token_secret=os.environ["X_ACCESS_SECRET"],
        )
        x_client.create_tweet(text=text)
        print(f"📡 放流完了: {text[:20]}")
    except Exception as e:
        print(f"❌ X Error: {e}")

if __name__ == "__main__":
    client = create_gemini_client()
    for lang in ["jp", "en"]:
        content = generate_akuh_content(client, lang)
        if content:
            post_to_x(content)
            time.sleep(10)
