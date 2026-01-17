import os
import requests

# 1. APIキー取得
api_key = os.environ.get("GEMINI_API_KEY")

# 2. 直接URLを指定（404を回避する最強の書き方）
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

payload = {
    "contents": [{"parts": [{"text": "「あくう」として一言、短い独白を日本語で。"}]}]
}

print("📡 Geminiと通信を開始します...")

try:
    response = requests.post(url, json=payload)
    data = response.json()
    
    if "candidates" in data:
        print("✅ 成功！Geminiの回答:")
        print(data["candidates"][0]["content"]["parts"][0]["text"])
    else:
        print("❌ エラー応答:")
        print(data)
except Exception as e:
    print(f"❌ 実行エラー: {e}")
