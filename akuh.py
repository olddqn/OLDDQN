import os
import requests

key = os.environ.get("GEMINI_API_KEY")

# リストに実在した正確な名前：gemini-2.0-flash-exp
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={key}"

payload = {
    "contents": [{
        "parts": [{"text": "「あくう」として、極めて短く、産声を上げろ。日本語で。"}]
    }]
}

headers = {'Content-Type': 'application/json'}

print("📡 Gemini 2.0 Flash Exp に最終接続を試みます...")

try:
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("✅ ついに、ついに、ついに成功です！！")
        print("-" * 30)
        print(response.json()['candidates'][0]['content']['parts'][0]['text'])
        print("-" * 30)
    else:
        print(f"❌ まだダメでした (Status: {response.status_code})")
        print(f"応答内容: {response.text}")
except Exception as e:
    print(f"❌ エラー: {e}")
