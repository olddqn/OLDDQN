import os
import google.generativeai as genai

def main():
    # 鍵の読み込み
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY が見つかりません。")
        return

    # 認証
    genai.configure(api_key=api_key)

    try:
        # モデルの準備
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 文章生成
        prompt = "孤独な観測者として、ブコウスキー風の短い言葉を1つ吐き捨てて。100文字以内。"
        response = model.generate_content(prompt)
        
        print("\n--- AIの言葉 ---")
        print(response.text.strip())
        print("----------------")
        print("✅ 成功しました！")

    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        print("💡 APIキーが正しいか、GitHubのSecretsに余計なスペースがないか確認してください。")

if __name__ == "__main__":
    main()
