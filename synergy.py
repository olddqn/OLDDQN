import os
import tweepy
import google.generativeai

# GitHubのSecretsに登録した名前を使います
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    try:
        # モデル名をシンプルに指定（404エラー対策）
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = "あなたは『あくう』。欲望を喰らう観測者として、130文字以内で独白せよ。"
        response = model.generate_content(prompt)
        msg = response.text.strip()
        print(f"📡 AI生成成功: {msg}")

        # Xへの投稿
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client.create_tweet(text=msg)
        print("✅ X投稿完了！")

    except Exception as e:
        print(f"❌ エラー発生: {e}")
        raise e

if __name__ == "__main__":
    main()
