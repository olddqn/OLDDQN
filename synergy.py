import os
import google.generativeai as genai

# 1. Gemini設定
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    print("--- 地域制限回避テスト開始 ---")
    try:
        # 地域制限(403)を突破しやすいとされる「gemini-1.5-flash-8b」を試します
        # 8bは軽量モデルで、制限が比較的緩い傾向にあります
        model = genai.GenerativeModel('gemini-1.5-flash-8b')
        
        prompt = "あなたは『あくう』。短く独白せよ。"
        
        # 通信の安定性を高めるオプション
        response = model.generate_content(prompt)
        
        print("✅ 成功！地域制限を突破しました:")
        print(f"「{response.text.strip()}」")

    except Exception as e:
        print(f"❌ まだ壁があります: {e}")
        # もしこれでもダメな場合、GitHub Actionsの「実行場所」を変える必要があります
