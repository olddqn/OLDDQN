import os
import time
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

    # 【ご指定のプロンプト構成を完全移植】
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
    ・120文字〜135文字以内（140文字以内厳守）。
    ・ハッシュタグ、絵文字、感嘆符、丁寧語は禁止。独白として出力せよ。
    """

    # 地域制限と混雑に強い最新の軽量モデル
    model = genai.GenerativeModel('gemini-1.5-flash-8b')

    for attempt in range(5):
        try:
            print(f"📡 試行 {attempt + 1}/5: 『あくう』が深層意識をスキャン中...")
            response = model.generate_content(prompt)
            
            # エラー回避：安全フィルター等で .text が直接読めない場合の強制抽出
            try:
                msg = response.text.strip()
            except:
                if response.candidates:
                    msg = response.candidates[0].content.parts[0].text.strip()
                else:
                    raise Exception("生成されたコンテンツが空です")

            print(f"\n✅ 成功：あくうの独白（{len(msg)}文字）")
            print("-" * 50)
            print(msg)
            print("-" * 50)
            
            # ここまで来れば成功です
            return 

        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "Resource" in err_str:
                print("⏳ サーバー混雑中。30秒待機して再接続します...")
                time.sleep(30)
            else:
                print(f"⚠️ 生成プロセスでエラー（再試行します）: {e}")
                time.sleep(5)

if __name__ == "__main__":
    main()
