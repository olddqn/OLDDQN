import os
import google.generativeai as genai

# Gemini設定
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    # 観測対象のノイズ（指定されたアカウント群）
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    # あなたが指定した究極のプロンプト
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
    ※130文字以内で出力せよ。
    """

    print("--- 魂の投影テスト開始 ---")
    try:
        # 成功した軽量・高回避モデルを使用
        model = genai.GenerativeModel('gemini-1.5-flash-8b')
        
        print("🤖 あくうが深層意識にダイブ中...")
        response = model.generate_content(prompt)
        msg = response.text.strip()
        
        print("\n✅ 生成された独白:")
        print("-" * 30)
        print(msg)
        print("-" * 30)
        print("\n--- テスト完了 ---")

    except Exception as e:
        print(f"❌ 生成エラー: {e}")
        raise e

if __name__ == "__main__":
    main()
