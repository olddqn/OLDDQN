import os
import google.generativeai as genai

def test_connection():
    print("🛠️ Gemini 接続テスト開始（原点回帰モード）...")
    
    try:
        # ルール1: APIキーをシンプルに設定
        genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
        
        # ルール2: モデル名は「gemini-1.5-flash」のみ（余計なパスを付けない）
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("📡 接続試行中...")
        
        # ルール3: 余計なRequestOptionsを使わず、直接生成を叩く
        response = model.generate_content("Hello. Are you there?")
        
        print(f"✅ 成功！Geminiの応答: {response.text}")
        print("\n✨ つながりました。この形が『絶対的なルール』です。")

    except Exception as e:
        print(f"❌ 接続失敗: {e}")

if __name__ == "__main__":
    test_connection()
