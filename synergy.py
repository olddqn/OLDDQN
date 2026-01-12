import os
import google.generativeai as genai

# 1. Gemini設定
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    try:
        # 【重要】403を突破しやすい「1.5-flash」を直接指定
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 5日前の雰囲気を再現した最小プロンプト
        prompt = "あなたは『あくう』。冷徹な観測者として、人間の欲望について100文字以内で独白せよ。"
        
        print("🤖 あくうが接続を試みています...")
        response = model.generate_content(prompt)
        
        # これがログに出れば「連携成功」です
        print(f"✅ 生成成功: {response.text.strip()}")

    except Exception as e:
        print(f"❌ まだ拒否されています: {e}")
        raise e

if __name__ == "__main__":
    main()
