import os
import tweepy
from google import genai

def main():
    # Geminiの最新クライアント設定
    client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
    
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    prompt = f"""
    あなたは『あくう』の観測者。欲望と毒に満ちた以下のノイズを喰らい、
    130文字以内で独白せよ（ハッシュタグ・絵文字・丁寧語は禁止）：
    {', '.join(targets)}
    """

    try:
        # 最新の生成方法 (モデル名に models/ は不要)
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        msg = response.text.strip()
        print(f"📡 生成された文章: {msg}")

        # Xへの投稿
        client_x = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client_x.create_tweet(text=msg)
        print("✅ Xへの投稿に成功しました")

    except Exception as e:
        # ログにエラーの内容をはっきり表示させる
        print(f"❌ 致命的なエラー: {e}")
        # Actionsを失敗（赤色）させて、問題があることを知らせる
        raise e

if __name__ == "__main__":
    main()
