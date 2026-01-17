import os
import requests

# APIキーはGitHubのSecretsから自動で入ります
key = os.environ.get("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"

payload = {
    "contents": [{"parts": [{"text": "「あくう」として一言、短い独白を日本語で。"}]}]
}

print("--- 通信開始 ---")
try:
    response = requests.post(url, json=payload)
    print(response.json()["candidates"][0]["content"]["parts"][0]["text"])
except Exception as e:
    print(f"失敗しました: {e}")
    # 失敗した時、何が起きたか生データを出す
    print(response.text)
