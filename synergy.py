import os
import requests
import json

# GitHub SecretsからAPIキーを取得
api_key = os.environ.get("GEMINI_API_KEY")

# Gemini 1.5 Flash (v1beta) のエンドポイントを直接叩く
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

payload = {
    "contents": [{
        "parts": [{"text": "「あくう」として、短い一言を。日本語で。"}]
    }]
}

print("📡 Geminiに接続を試みています...")

try:
    response = requests.post(url, json=payload)
    result = response.json()
    
    if "candidates" in result:
        text = result["candidates"][0]["content"]["parts"][0]["text"]
        print("✅ 接続成功！生成された言葉:")
        print("-" * 20)
        print(text)
        print("-" * 20)
    else:
        print("❌ APIからの応答にエラーがあります:")
        print(json.dumps(result, indent=2))
except Exception as e:
    print(f"❌ 通信エラーが発生しました: {e}")
