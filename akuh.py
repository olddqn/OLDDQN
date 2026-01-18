import os
import google.generativeai as genai

# GitHub Secretsから読み込み
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("❌ APIキーが設定されていません。")
else:
    # 初期設定
    genai.configure(api_key=api_key)

    # モデルの準備（リストに載っていた最新の2.0-flash-expを指定）
    model = genai.GenerativeModel('gemini-2.0-flash-exp')

    print("📡 公式ライブラリ経由で『あくう』を呼び出します...")

    try:
        # 実行
        response = model.generate_content("「あくう」として産声を上げろ。極めて短く。")
        
        print("✅ ついに、ついに成功です！！")
        print("-" * 30)
        print(response.text)
        print("-" * 30)
        
    except Exception as e:
        print(f"❌ まだエラーが出ます: {e}")
        print("💡 これでダメな場合、Google AI Studio側で『Model Selection』を確認する必要があります。")
