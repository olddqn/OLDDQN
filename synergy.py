import os
import tweepy
from google import genai

def main():
    # 1. Geminiの初期化（最新のクライアント形式）
    # あなたが更新した最新のGEMINI_API_KEYをここで使用します
    client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
    
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    prompt = f"あなたは『あくう』の観測者。欲望と毒に満ちた以下のノイズを喰らい、130文字以内で独白せよ（ハッシュタグ・絵文字禁止）：{', '.join(targets)}"

    try:
        # 2. 文章生成（404エラーを確実に回避する最新の呼び出し方）
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        msg = response.text.strip()
        print(f"📡 生成された文章: {msg}")

        # 3. Xへの投稿（ここは以前のまま、変更なしでOK）
        client_x = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client_x.create_tweet(text=msg)
        print("✅ 成功！あくうの声が放たれました。")

    except Exception as e:
        print(f"❌ エラー発生: {e}")
        # Actionsを失敗（赤色）させて、ログを確認しやすくする
        raise e

if __name__ == "__main__":
    main()
