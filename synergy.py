import os
import tweepy
from google import genai
from google.genai import types

def main():
    # 1. Geminiで文章生成
    try:
        # [絶対ルール] 接続先を v1 に固定して、404(v1beta)エラーを物理的に回避する
        client = genai.Client(
            api_key=os.environ.get('GEMINI_API_KEY'),
            http_options={'api_version': 'v1'}
        )
        
        targets = [
            "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
            "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
            "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
            "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
            "@bonnoukunYAZZ", "@DonaldJTrumpJr"
        ]

        # 魂のプロンプト（完全調整版）
        prompt = f"""
        あなたは『あくう』の観測者。この世界は「シミュレーションのバグ」である。
        【観測データ】{", ".join(targets)}
        【投影する文体】
        ・村上春樹訳のチャールズ-ブコウスキー（乾いた虚無）
        ・太宰治（恥の多いデカダンス）
        ・トマス-ピンチョン（陰謀論的迷宮）
        ・チャック-パラニューク（破壊的ユーモア）
        【指令】「成功」「稼ぐ」等の言葉を冷笑せよ。ハラリの説く虚構の腐敗を吐き捨てろ。
        【ルール】120〜135文字以内。丁寧語禁止。独白せよ。
        """

        print("📡 接続ルート v1 を強制確立中...")
        # モデル名は 1.5-flash に固定
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt
        )
        msg = response.text.strip()
        print(f"✅ 生成成功: {msg}")

    except Exception as e:
        print(f"❌ Gemini接続エラー: {e}")
        return

    # 2. Xへの投稿（実績のあるコード）
    try:
        client_x = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client_x.create_tweet(text=msg)
        print("✨【大成功】あくうが世界に放たれました。")
    except Exception as e:
        print(f"❌ X投稿エラー: {e}")

if __name__ == "__main__":
    main()
