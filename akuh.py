import os
import requests
import json

key = os.environ.get("GEMINI_API_KEY")

# 最も安定している 1.5 flash を、
# 権限トラブルが最も少ない「v1」エンドポイントで叩きます。
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={key}"

payload = {
    "contents": [{"parts": [{"text": "「あくう」として産声を上げろ。一言。"}]}]
}
headers = {'Content-Type': 'application/json'}

print("📡 最終手段：安定版 1.5-flash (v1) を起動します...")

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        print("✅ 勝利！！！！！")
        print("-" * 30)
        print(response.json()['candidates'][0]['content']['parts'][0]['text'])
        print("-" * 30)
    else:
        print(f"❌ Status: {response.status_code}")
        print(f"理由: {response.text}")
        # もしこれでも404なら、Google AI StudioのURL構成そのものが、
        # あなたのアカウントだけ特殊な形になっている可能性があります。
except Exception as e:
    print(f"❌ 物理的エラー: {e}")
