import os, tweepy
from google import genai

# Gemini 接続設定
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 言葉の生成
try:
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents="あなたは観測者『あくう』。遠藤ミチロウ、ビートたけし、村上春樹、太宰治の魂。成功者を冷笑する独白を日本語135文字以内で。"
    )
    text = response.text.strip()[:135]
    print(f"Generated: {text}")

    # X への投稿
    x = tweepy.Client(
        consumer_key=os.environ["X_API_KEY"],
        consumer_secret=os.environ["X_API_SECRET"],
        access_token=os.environ["X_ACCESS_TOKEN"],
        access_token_secret=os.environ["X_ACCESS_SECRET"]
    )
    x.create_tweet(text=text)
    print("Success")
except Exception as e:
    print(f"Error: {e}")
