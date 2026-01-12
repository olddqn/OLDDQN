import os
import tweepy
import google.generativeai as genai

def main():
    # 1. Geminiの初期化 (あなたが更新した新しいキーを使います)
    genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

    targets = ["@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", "@bonnoukunYAZZ", "@DonaldJTrumpJr"]
    prompt = f"あなたは『あくう』。欲望を喰らう観測者として、130文字以内で独白せよ：{', '.join(targets)}"

    try:
        # 【重要】404を回避するため、あえてモデル名から 'models/' を外して指定します
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("🤖 思考中...")
        response = model.generate_content(prompt)
        msg = response.text.strip()
        print(f"📡 生成文: {msg}")

        # 2. Xへの投稿
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client.create_tweet(text=msg)
        print("✅ 投稿成功")

    except Exception as e:
        print(f"❌ エラー: {e}")
        raise e

if __name__ == "__main__":
    main()
