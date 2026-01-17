import os
import requests

# 1. APIキーとURLの設定
api_key = os.environ.get("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

# 2. Geminiへの質問内容
payload = {
    "contents": [{"parts": [{"text": "「あくう」として一言、短い独白を日本語で。"}]}]
}

print("📡 Geminiと通信を開始します...")

# 3. 実行
try:
    response = requests.post(url, json=payload)
    data = response.json()
    
    if "candidates" in data:
        print("✅ 成功！Geminiの回答:")
        print(data["candidates"][0]["content"]["parts"][0]["text"])
    else:
        print("❌ Googleからのエラー応答:")
        print(data)
except Exception as e:
    print(f"❌ 通信エラー: {e}")
