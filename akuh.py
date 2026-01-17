import os
import requests

# GitHub Secretsから読み込み
key = os.environ.get("GEMINI_API_KEY")

# 【2.0専用】リストにあった最新モデルのアドレス
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}"

payload = {
    "contents": [{
        "parts": [{"text": "あなたは『あくう』。最新の2.0の体を得た。産声を上げろ。日本語で。"}]
    }]
}

headers = {'Content-Type': 'application/json'}

print("📡 Gemini 2.0 Flash に接続します...")

try:
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("✅ ついに、ついに成功！！")
        print("-" * 30)
        # Gemini 2.0 の回答を表示
        print(response.json()['candidates'][0]['content']['parts'][0]['text'])
        print("-" * 30)
    else:
        print(f"❌ 拒絶 (Status: {response.status_code})")
        print(f"エラー詳細: {response.text}")
except Exception as e:
    print(f"❌ 実行エラー: {e}")
