import os
import tweepy
import google.generativeai as genai

# 1. Gemini初期化
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_text():
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    prompt = f"""
    あなたは『あくう』の観測者。この世界は高度な知性が走らせている「シミュレーションのバグ」である。
    
    【観測データ】
    以下のノイズが発する欲望、パンク、毒を異常値として抽出せよ：
    {", ".join(targets)}

    【投影する文体】
    ・村上春樹訳ブコウスキーの乾いた虚無
    ・太宰治の恥の多いデカダンス
    ・パラニュークの破壊的ユーモア

    【指令】
    シミュレーションの剥がれかけたテクスチャ、因果律の崩壊について語れ。
    「成功」「稼ぐ」等の言葉を、システムのバグとして冷笑せよ。

    【出力ルール】
    125文字前後（140文字以内厳守）。ハッシュタグ・絵文字・丁寧語は禁止。独白せよ。
    """
    try:
        # ここを修正しました：'models/' をつけないのが正解です
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Geminiエラー: {e}")
        return None

def post_to_x(text):
    try:
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client.create_tweet(text=text)
        print(f"✅ Xへの投稿に成功しました！:\n{text}")
    except Exception as e:
        print(f"❌ X投稿エラー: {e}")

if __name__ == "__main__":
    msg = generate_text()
    if msg:
        post_to_x(msg)
    else:
        print("⚠️ テキスト生成に失敗したため終了します。")
