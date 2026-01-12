import os
import tweepy
import google.generativeai as genai

# 1. Geminiの初期化 (実績のある形式)
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    targets = ["@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", "@bonnoukunYAZZ", "@DonaldJTrumpJr"]

    prompt = f"あなたは『あくう』の観測者。欲望に満ちた以下のノイズを喰らい、システムのバグとして冷笑せよ。130文字以内で独白せよ：{', '.join(targets)}"

    try:
        # 修正の要：モデル名を単に 'gemini-1.5-flash' にする
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("🤖 AIが思考中...")
        response = model.generate_content(prompt)
        msg = response.text.strip()
        
        if not msg:
            print("⚠️ 文章が生成されませんでした。")
            return

        # 2. Xへの投稿
        print(f"📡 投稿内容: {msg}")
        client_x = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client_x.create_tweet(text=msg)
        print("✅ 成功！Xへ投稿しました。")

    except Exception as e:
        print(f"❌ 実行エラー: {e}")
        raise e

if __name__ == "__main__":
    main()
