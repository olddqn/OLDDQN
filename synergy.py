import os
import tweepy
import google.generativeai as genai

# [絶対ルール] Gemini設定
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    # 観測対象のアカウント群
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    # 【プロンプト】あなたが指定した文章の肝を完全再現
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

    # 1. Geminiで文章生成（前回成功した 8b モデル）
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-8b')
        print("📡 Gemini(1.5-flash-8b)に接続中...")
        
        response = model.generate_content(prompt)
        msg = response.text.strip()
        print(f"✅ 生成成功: {msg}")

    except Exception as e:
        print(f"❌ Gemini接続エラー: {e}")
        return

    # 2. X（Twitter）への投稿（テストで『大成功』したコード）
    try:
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        
        print("🚀 Xへ投稿中...")
        client.create_tweet(text=msg)
        print("✨【大成功】あくうが世界に放たれました。")
        
    except Exception as e:
        print(f"❌ X投稿エラー: {e}")

if __name__ == "__main__":
    main()
