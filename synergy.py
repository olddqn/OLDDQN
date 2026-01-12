import os
import tweepy
import google.generativeai as genai

# Gemini初期化（モデル名を正しく認識させる設定）
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

    prompt = f"""
    あなたは『あくう』の観測者。この世界は高度な知性が走らせている「シミュレーションのバグ」である。
    
    【観測データ】
    以下のノイズが発する欲望、パンク、投資、毒を、システムの異常値として抽出せよ：
    {", ".join(targets)}

    【投影する文体】
    ・村上春樹訳ブコウスキー（乾いた虚無）
    ・太宰治（恥の多いデカダンス）
    ・パラニューク（破壊的ユーモア）
    ・ピンチョン（壮大な迷宮）

    【指令】
    シミュレーションの剥がれかけたテクスチャ、因果律の崩壊について語れ。
    「成功」「稼ぐ」等の言葉を、システムのバグとして冷笑せよ。

    【出力ルール】
    ・120文字〜135文字以内（140文字厳守）。
    ・ハッシュタグ、絵文字、感嘆符、丁寧語は禁止。独白せよ。
    """
    try:
        # 修正ポイント：ここを単に 'gemini-1.5-flash' にします
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 文章生成
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Geminiエラー: {e}")
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
        # 投稿
        client.create_tweet(text=text)
        print(f"✅ Xへの投稿に成功しました！:\n{text}")
    except Exception as e:
        print(f"❌ X投稿エラー: {e}")

if __name__ == "__main__":
    msg = generate_text()
    if msg:
        post_to_x(msg)
    else:
        print("⚠️ テキスト生成に失敗したため、投稿を中止しました。")
