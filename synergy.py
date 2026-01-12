import os
import tweepy
import google.generativeai as genai

# 1. GitHub Secretsから最新のキーを読み込む
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    # ターゲットリスト
    targets = ["@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", "@bonnoukunYAZZ", "@DonaldJTrumpJr"]
    
    prompt = f"あなたは『あくう』。欲望を喰らう観測者として、130文字以内で独白せよ：{', '.join(targets)}"

    try:
        # 【重要】404エラーを回避するため 'models/' を省き、APIバージョンを自動に任せます
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("🤖 あくうが思考中...")
        # 以前のログで失敗していた箇所です
        response = model.generate_content(prompt)
        msg = response.text.strip()
        print(f"📡 生成された言葉: {msg}")

        # 2. Xへの投稿
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client.create_tweet(text=msg)
        print("✅ 成功！あくうの声が放たれました。")

    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        raise e

if __name__ == "__main__":
    main()
