import os
import time
import tweepy
import google.generativeai as genai

# Gemini設定
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

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
    ・120文字〜135文字以内。
    ・ハッシュタグ、絵文字、感嘆符、丁寧語は禁止。独白として出力せよ。
    """

    # 1. Geminiで生成（モデル名をより汎用的なものに変更）
    model = genai.GenerativeModel('gemini-1.5-flash')
    msg = ""

    for attempt in range(5):
        try:
            print(f"📡 試行 {attempt + 1}/5: 接続中...")
            response = model.generate_content(prompt)
            try:
                msg = response.text.strip()
            except:
                if response.candidates:
                    msg = response.candidates[0].content.parts[0].text.strip()
            
            if msg:
                print(f"✅ 生成成功: {msg}")
                break
        except Exception as e:
            print(f"⏳ 待機中... ({e})")
            time.sleep(30)

    if not msg:
        print("❌ 生成に失敗しました。")
        return

    # 2. X（Twitter）へ投稿（先ほど成功した設定を使用）
    try:
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client.create_tweet(text=msg)
        print("🚀 大成功！あくうが世界に放たれました。")
    except Exception as e:
        print(f"❌ X投稿エラー: {e}")

if __name__ == "__main__":
    main()
