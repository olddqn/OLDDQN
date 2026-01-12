import os
import time
import google.generativeai as genai
from google.api_core import exceptions

# Gemini設定
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    # 観測対象のノイズ
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    # 改良された高密度プロンプト
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
    ・120文字から135文字以内を死守せよ（最大140文字）。
    ・ハッシュタグ、絵文字、丁寧語、感嘆符は一切禁止。
    ・システムログのような冷徹な独白のみを出力せよ。
    """

    # 接続の安定性を考慮し、1.5-flash-8bを使用
    model = genai.GenerativeModel('gemini-1.5-flash-8b')

    # 混雑対策のリトライ
    for attempt in range(3):
        try:
            print(f"📡 あくうが深層意識をスキャン中... ({attempt + 1}回目)")
            response = model.generate_content(prompt)
            msg = response.text.strip()
            
            # 文字数確認
            char_count = len(msg)
            print(f"\n✅ 独白生成（{char_count}文字）:")
            print("-" * 40)
            print(msg)
            print("-" * 40)
            
            # ここまで来れば成功です
            return 

        except exceptions.ResourceExhausted:
            print("⏳ サーバー混雑。15秒待機して再接続します。")
            time.sleep(15)
        except Exception as e:
            print(f"❌ エラー発生: {e}")
            break

if __name__ == "__main__":
    main()
