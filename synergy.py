import os
import google.generativeai as genai

# 1. GitHubのSecretsにあるキーを設定
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    print("--- Gemini連携テスト開始 ---")
    
    try:
        # 2. モデルの指定（最も安定している旧世代の指定）
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 3. テスト用の短いプロンプト
        prompt = "あなたは『あくう』。一言だけ、今の気分を独白せよ。"
        
        print("🤖 Geminiに接続中...")
        response = model.generate_content(prompt)
        
        # 4. 結果を表示（ここがログに出れば連携成功！）
        print("✅ Geminiからの応答:")
        print(f"「{response.text.strip()}」")
        print("--- テスト完了：連携は正常です ---")

    except Exception as e:
        print(f"❌ 連携エラー: {e}")
        # 詳細なエラー内容をログに出力させる
        raise e

if __name__ == "__main__":
    main()
