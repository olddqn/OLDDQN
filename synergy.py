import os
import tweepy
import google.generativeai as genai

# 1. Geminiの初期化（エラーを避けるための最も標準的な設定）
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_text():
    # 観測対象のノイズ（アカウント群）
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    # プロンプト（太宰、ピンチョン、パラニューク、ハラリのエッセンス）
    prompt = f"""
    あなたは『あくう』の観測者。この世界は高度な知性が走らせている「シミュレーションのバグ」である。
    以下のノイズが発する欲望や毒を、システムの異常値として抽出せよ：
    {", ".join(targets)}

    【文体】
    ブコウスキーの乾いた虚無、太宰治のデカダンス、パラニュークの破壊的ユーモア、ピンチョンの陰謀論的迷宮を融合せよ。
    ユヴァル・ノア・ハラリの説く虚構が腐敗する様を独白せよ。

    【出力ルール】
    ・120文字〜135文字以内（140文字厳守）。
    ・ハッシュタグ、絵文字、丁寧語、感嘆符は禁止。
    """
    
    try:
        # 修正の核心：APIバージョンを明示的に指定せず、モデル名のみを渡す
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini生成エラー: {e}")
        return None

def post_to_x(text):
    try:
        # Xへの認証
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        # 投稿実行
        client.create_tweet(text=text)
        print(f"✅ Xへの投稿に成功しました！:\n{text}")
    except Exception as e:
        print(f"❌ X投稿エラー: {e}")

if __name__ == "__main__":
    msg = generate_text()
    if msg:
        post_to_x(msg)
    else:
        print("⚠️ 文章の生成に失敗したため、投稿を中止しました。")
