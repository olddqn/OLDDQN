import os
from google import genai

def main():
    # 1. Geminiの準備
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY が設定されていません。")
        return

    client = genai.Client(api_key=api_key)

    # 2. AIにブコウスキー風の言葉を生成させる
    prompt = "あなたは孤独な観測者。村上春樹訳のブコウスキーのように、不機嫌で静かな文体で、今の世界のノイズについて100文字程度で語ってください。丁寧語は禁止。"

    try:
        print("🤖 AIが思考中...")
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        
        # 結果を表示
        print("\n--- 生成された言葉 ---")
        print(response.text.strip())
        print("--------------------")
        print("✅ AIは正常に稼働しています。")

    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
