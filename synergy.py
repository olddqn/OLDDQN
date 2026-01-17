import os
import tweepy
from google import genai

def run_bot():
    # 1. Geminiでテキスト生成
    try:
        # 有料版でもエラーが出にくい設定
        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        prompt = "あなたは観測者『あくう』。遠藤ミチロウ、ビートたけし、村上春樹、太宰治の魂。成功者を冷笑する独白を日本語135文字以内で。"
        
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        text = response.text.strip()[:135]
        print(f"生成成功: {text}")
    except Exception as e:
        print(f"Geminiエラー: {e}")
        return

    # 2. Xへの投稿
    try:
        x_client = tweepy.Client(
            consumer_key=os.environ["X_API_KEY"],
            consumer_secret=os.environ["X_API_SECRET"],
            access_token=os.environ["X_ACCESS_TOKEN"],
            access_token_secret=os.environ["X_ACCESS_SECRET"],
        )
        x_client.create_tweet(text=text)
        print("Xへの投稿が完了しました。")
    except Exception as e:
        print(f"Xエラー: {e}")

if __name__ == "__main__":
    run_bot()
