import os
import requests

# GitHub Secretsから読み込み
key = os.environ.get("GEMINI_API_KEY")

# 【最重要】404を回避するための「黄金のURL」
# v1beta ではなく v1 を使い、末尾の :generateContent まで正確に指定します
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={key}"

payload = {
    "contents": [{
        "parts": [{"text": "あなたは『あくう』。短い一言を。日本語で。"}]
    }]
}

headers = {'Content-Type': 'application/json'}

print("📡 最終接続テスト（v1/models形式）を開始...")

try:
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("✅ ついに成功！！")
        print("-" * 30)
        print(response.json()['candidates'][0]['content']['parts'][0]['text'])
        print("-" * 30)
    else:
        print(f"❌ まだ拒絶 (Status: {response.status_code})")
        print(f"応答内容: {response.text}")
except Exception as e:
    print(f"❌ エラー発生: {e}")
