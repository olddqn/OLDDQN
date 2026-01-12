import os
import google.generativeai as genai
from google.generativeai.types import RequestOptions

def test_connection():
    print("🛠️ Gemini 接続テスト開始...")
    
    try:
        # APIキー設定
        genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
        
        # [絶対ルール] 404を回避するために v1 (安定版) を明示的に指定
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("📡 モデルを呼び出し中 (API Version: v1)...")
        
        # 最も軽いリクエストで接続確認
        response = model.generate_content(
            "Hello",
            request_options=RequestOptions(api_version='v1')
        )
        
        print(f"✅ 接続成功！応答: {response.text}")
        print("--- これで『脳』は生きています ---")

    except Exception as e:
        print(f"❌ 接続失敗: {e}")
        print("\n💡 ヒント: もし404が出るなら、APIキーが古いか、Google側のモデル名変更が反映されています。")

if __name__ == "__main__":
    test_connection()
