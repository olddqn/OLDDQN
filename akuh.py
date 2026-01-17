import os, tweepy
from google import genai

# 設定
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
p = "あなたは『あくう』。遠藤ミチロウ、ビートたけし、村上春樹、太宰治の魂。成功者を冷笑する独白を日本語135文字以内で。"

# 生成と投稿（インデントは半角スペース1つだけにしています）
try:
 r = client.models.generate_content(model="gemini-1.5-flash", contents=p)
 t = r.text.strip()[:135]
 print(f"Text: {t}")
 x = tweepy.Client(
  consumer_key=os.environ["X_API_KEY"],
  consumer_secret=os.environ["X_API_SECRET"],
  access_token=os.environ["X_ACCESS_TOKEN"],
  access_token_secret=os.environ["X_ACCESS_SECRET"]
 )
 x.create_tweet(text=t)
 print("Success")
except Exception as e:
 print(f"Error: {e}")
