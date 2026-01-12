import os
import tweepy
import google.generativeai as genai

# 1. Geminiの設定（もっとも安定していた旧世代の書き方）
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    # ターゲット（観測対象）
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    try:
        # --- Geminiによる独白生成 ---
        # 403エラーを避けるため、1.5ではなく「gemini-pro」を指名
        model = genai.GenerativeModel('gemini-pro')
        
        # プロンプト（独白に集中）
        prompt = f"あなたは『あくう』という名の冷徹な観測者。以下の者たちの欲望を嘲笑し、130文字以内で独白せよ（ハッシュタグ・絵文字禁止）：{', '.join(targets)}"
        
        print("🤖 あくうが思考を開始...")
        response = model.generate_content(prompt)
        msg = response.text.strip()
        print(f"📡 生成されたメッセージ: {msg}")

        # --- Xへの投稿 ---
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        
        client.create_tweet(text=msg)
        print("✅ 投稿成功。あくうの独白が放たれました。")

    except Exception as e:
        print(f"❌ エラー発生: {e}")
        # 万が一エラーが出た際、ログに詳細を残す
        raise e

if __name__ == "__main__":
    main()
