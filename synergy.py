import os
import tweepy
from google import genai

def main():
    # 1. Geminiの初期化（最新のクライアント形式）
    # APIキーはGitHubのSecretsから自動で読み込まれます
    client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
    
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    prompt = f"""
    あなたは『あくう』の観測者。この世界は高度な知性が走らせている「シミュレーションのバグ」である。
    以下のノイズが発する欲望や毒を、システムの異常値として抽出せよ：
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
    ・ハッシュタグ、絵文字、丁寧語、感嘆符は禁止。独白せよ。
    """

    try:
        # 2. 文章生成（404エラーを回避する最新の呼び出し方）
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        msg = response.text.strip()
        print(f"📡 生成された文章: {msg}")

        # 3. Xへの投稿
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
        raise e

if __name__ == "__main__":
    main()
