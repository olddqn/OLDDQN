import os
import time
import google.generativeai as genai

# 1. Gemini設定
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    targets = ["@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", "@bonnoukunYAZZ", "@DonaldJTrumpJr"]

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
    ・ハッシュタグ、絵文字、丁寧語、感嘆符は一切禁止。独白せよ。
    """

    model = genai.GenerativeModel('gemini-1.5-flash-8b')

    # リトライ回数を増やし、判定を「確実」なものに変更
    for attempt in range(5):
        try:
            print(f"📡 あくう：接続試行中... ({attempt + 1}回目)")
            response = model.generate_content(prompt)
            msg = response.text.strip()
            
            print(f"\n✅ 魂の投影に成功しました（{len(msg)}文字）:")
            print("-" * 40)
            print(msg)
            print("-" * 40)
            return # 成功したらここで終了

        except Exception as e:
            # エラーメッセージの中に「429」や「Resource」が含まれていたらリトライ
            error_str = str(e)
            if "429" in error_str or "Resource" in error_str:
                print(f"⏳ サーバーが混雑しています。30秒待機します...")
                time.sleep(30)
            else:
                print(f"❌ 予期せぬエラーが発生しました: {e}")
                break

if __name__ == "__main__":
    main()
