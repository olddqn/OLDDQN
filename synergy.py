import os
import tweepy
import google.generativeai as genai

# [絶対ルール] 設定はこれだけでいい
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_text():
    # 観測対象
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    # プロンプト構成（魂の定義）
    prompt = f"""
    あなたは『あくう』の観測者。この世界は、ある高度な知性が走らせている「シミュレーションのバグ」である。
    【観測データ】{", ".join(targets)}
    【投影する文体】
    ・村上春樹訳のチャールズ-ブコウスキー（乾いた虚無）
    ・太宰治（恥の多いデカダンス）
    ・トマス-ピンチョン（陰謀論的迷宮）
    ・チャック-パラニューク（破壊的ユーモア）
    【指令】
    シミュレーションの剥がれかけたテクスチャ、因果律の崩壊について語れ。
    「成功」「稼ぐ」等の言葉を、システムのバグとして冷笑せよ。
    ハラリの説く「虚構」が、電子の海で腐敗していく様を吐き捨てろ。
    【出力ルール】
    ・120文字〜135文字（140文字以内厳守）。
    ・ハッシュタグ、絵文字、感嘆符、丁寧語は禁止。独白として出力せよ。
    """
    
    # 404を回避するため、モデル名だけをシンプルに指定
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # [重要] サーバーのバージョンを強制的に「v1」に固定して呼び出す
    response = model.generate_content(prompt)
    return response.text.strip()

def main():
    print("📡 観測開始...")
    try:
        # 1. 文章生成
        msg = generate_text()
        print(f"✅ 生成成功: {msg}")

        # 2. Xへの投稿（実績のあるコード）
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client.create_tweet(text=msg)
        print("✨【大成功】あくうが世界に放たれました。")

    except Exception as e:
        print(f"❌ エラー発生: {e}")

if __name__ == "__main__":
    main()
