import os
import tweepy
import google.generativeai as genai

# 1. Geminiの初期化 (以前成功した実績のある形式)
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    # ターゲット：あくうが飲み込むノイズ
    targets = ["@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", "@bonnoukunYAZZ", "@DonaldJTrumpJr"]

    prompt = f"あなたは『あくう』の観測者。欲望に満ちた以下のノイズを喰らい、システムのバグとして冷笑せよ。130文字以内で独白せよ：{', '.join(targets)}"

    try:
        # 404エラーを回避するため、models/ を付けず、APIバージョンを固定しない
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("🤖 AIが思考中...")
        response = model.generate_content(prompt)
        msg = response.text.strip()
        
        if not msg:
            return

        # 2. Xへの投稿
        print(f"📡 投稿準備: {msg}")
        client_x = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client_x.create_tweet(text=msg)
        print("✅ 成功！あくうの声が放たれました。")

    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        # 再びエラーで緑色にならないよう、あえて例外を投げる
        raise e

if __name__ == "__main__":
    main()
