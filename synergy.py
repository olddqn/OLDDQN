import os
import google.generativeai as genai

def main():
    # 1. 鍵の取得
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY が設定されていません。")
        return

    # 2. 認証設定
    genai.configure(api_key=api_key)

    # 3. 生成
    try:
        # モデルの指定
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = "あなたは孤独な観測者。ブコウスキー風の短い言葉を1つ。100文字以内。"
        response = model.generate_content(prompt)
        
        print("\n--- AIが生成した言葉 ---")
        print(response.text.strip())
        print("-----------------------")
        print("✅ ついにAIとの接続に成功しました！")

    except Exception as e:
        print(f"❌ 実行エラー: {e}")

if __name__ == "__main__":
    main()
