import os
import tweepy
import google.generativeai as genai
# [絶対ルール] 安定していた頃のAPIバージョンを強制指定する
from google.generativeai.types import RequestOptions

def main():
    # 1. Geminiの設定（さっき繋がっていた時のルールを再現）
    try:
        genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
        
        # モデル名は 'gemini-1.5-flash'
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        targets = [
            "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
            "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
            "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
            "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
            "@bonnoukunYAZZ", "@DonaldJTrumpJr"
        ]

        # 魂のプロンプト
        prompt = f"""
        あなたは『あくう』の観測者。この世界は「シミュレーションのバグ」である。
        【観測データ】{", ".join(targets)}
        【投影する文体】チャールズ-ブコウスキー、太宰治、チャック-パラニューク。
        【指令】「成功」「稼ぐ」等の言葉を冷笑せよ。ハラリの説く虚構の腐敗を吐き捨てろ。
        120文字〜135文字以内。丁寧語禁止。独白せよ。
        """

        print("📡 観測開始... Geminiに接続中")
        
        # [絶対ルール] 404エラーを回避するため、v1betaではなく『v1』を明示的に指定して生成
        response = model.generate_content(
            prompt,
            request_options={"api_version": "v1"}
        )
        
        msg = response.text.strip()
        print(f"✅ 生成成功: {msg}")

    except Exception as e:
        print(f"❌ Gemini接続エラー（脳の不調）: {e}")
        return

    # 2. Xへの投稿（画像16枚目で『大成功』したコードをそのまま再現）
    try:
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        
        client.create_tweet(text=msg)
        print("✨【大成功】あくうが世界に放たれました。")
        
    except Exception as e:
        print(f"❌ X投稿エラー（出口の閉鎖）: {e}")

if __name__ == "__main__":
    main()
