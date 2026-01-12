import os
import time
import tweepy
from google import genai

def main():
    # 1. Gemini(最新SDK)で文章生成
    try:
        client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
        
        targets = [
            "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
            "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
            "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
            "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
            "@bonnoukunYAZZ", "@DonaldJTrumpJr"
        ]

        # あなたが守り抜いた魂のプロンプト
        prompt = f"""
        あなたは『あくう』の観測者。この世界は、ある高度な知性が走らせている「シミュレーションのバグ」である。
        
        【観測データ（サンプリング対象）】
        以下のノイズが発する欲望、投資、競馬、パンク、毒を、システムの異常値として抽出せよ：
        {", ".join(targets)}

        【投影する作家の文体】
        ・村上春樹訳のチャールズ-ブコウスキー（乾いた虚無）
        ・太宰治（恥の多いデカダンス）
        ・トマス-ピンチョン（陰謀論的迷宮）
        ・チャック-パラニューク（破壊的ユーモア）

        【指令】
        シミュレーションの剥がれかけたテクスチャ、因果律の崩壊について語れ。
        「成功」「稼ぐ」等の言葉を、システムのバグとして冷笑せよ。
        ハラリの説く「虚構」が、電子の海で腐敗していく様を吐き捨てろ。

        【出力ルール】
        ・120文字〜135文字以内（140文字厳守）。
        ・ハッシュタグ、絵文字、感嘆符、丁寧語は禁止。独白として出力せよ。
        """

        print("📡 通信路を確立。観測を開始します...")
        
        # モデルを安定版の 1.5-flash に固定し、制限にかかりにくくします
        response = client_gemini.models.generate_content(
            model='gemini-1.5-flash', 
            contents=prompt
        )
        msg = response.text.strip()
        print(f"✅ 生成成功: {msg}")

    except Exception as e:
        print(f"❌ Gemini接続エラー: {e}")
        # 429エラー(制限)が出た場合に備え、少し待ってから1回だけリトライする仕組み
        if "429" in str(e):
            print("⏳ 制限回避のため10秒待機してリトライします...")
            time.sleep(10)
            # リトライ実行
            response = client_gemini.models.generate_content(model='gemini-1.5-flash', contents=prompt)
            msg = response.text.strip()
            print(f"✅ リトライ成功: {msg}")
        else:
            return

    # 2. Xへの投稿（成功実績のあるコード）
    try:
        client_x = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client_x.create_tweet(text=msg)
        print("✨【成功】あくうが世界に放たれました。")
    except Exception as e:
        print(f"❌ X投稿エラー: {e}")

if __name__ == "__main__":
    main()
