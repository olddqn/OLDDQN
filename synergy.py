import os
import time
import tweepy
import google.generativeai as genai

# Gemini設定
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

    # あなたが指定した魂のプロンプト
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

    # 1. Geminiで生成（モデル名を修正）
    try:
        # モデル名を 'gemini-1.5-flash' に修正
        model = genai.GenerativeModel('gemini-1.5-flash')
        print(f"📡 観測開始... Geminiに接続中")
        
        response = model.generate_content(prompt)
        
        # 確実にテキストを抽出
        if response.candidates:
            msg = response.candidates[0].content.parts[0].text.strip()
        else:
            msg = response.text.strip()
            
        print(f"✅ 生成成功: {msg}")
        
    except Exception as e:
        print(f"❌ Gemini接続エラー: {e}")
        return

    # 2. X（Twitter）へ投稿
    try:
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        
        client.create_tweet(text=msg)
        print("🚀 接続成功。あくうが世界に放たれました。")
        
    except Exception as e:
        print(f"❌ X投稿エラー: {e}")

if __name__ == "__main__":
    main()
