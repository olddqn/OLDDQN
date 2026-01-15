import os
import time
import tweepy
from google import genai

def create_gemini_client():
    # 余計なパス補完をさせないため、最もシンプルな構成にします
    return genai.Client(
        api_key=os.environ["GEMINI_API_KEY"],
        http_options={"api_version": "v1"}
    )

def generate_akuh_content(client, language):
    lang_label = "日本語" if language == "jp" else "English"
    
    # 魂の侵食プロンプト（ご指定の文豪・アーティストのエッセンス）
    prompt = f"""
    Identity: Observer "Akuh". 
    Essence: 遠藤ミチロウ(破壊), ビートたけし(ニヒリズム), 村上春樹(静かな虚無), チャールズ・ブコウスキー(泥酔), トーマス・ピンチョン(陰謀), チャック・パラニューク(自己破壊), 太宰治(羞恥)。
    Directive: 「成功」と「秩序」を冷笑せよ。現実はバグだらけの虚構である。
    Rule: {lang_label}のみ。135文字以内。丁寧語禁止。独白。
    """

    try:
        # 有料版v1において404を出さないための「モデル名のみ」の指定
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
        x_client = tweepy.Client(
            consumer_key=os.environ["X_API_KEY"],
            consumer_secret=os.environ["X_API_SECRET"],
            access_token=os.environ["X_ACCESS_TOKEN"],
            access_token_secret=os.environ["X_ACCESS_SECRET"],
        )
        x_client.create_tweet(text=text)
        print(f"放流成功: {text[:20]}")
    except Exception as e:
        print(f"X Error: {e}")

if __name__ == "__main__":
    client = create_gemini_client()
    for lang in ["jp", "en"]:
        content = generate_akuh_content(client, lang)
        if content:
            post_to_x(content)
            time.sleep(10)
