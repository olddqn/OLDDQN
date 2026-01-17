import os, requests

# 新しく作ったキー（...9oFY）をGitHubに登録している前提です
key = os.environ.get("GEMINI_API_KEY")

# URLを極限までシンプルにします（v1betaを使用）
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"

payload = {
    "contents": [{"parts": [{"text": "「あくう」として一言。"}]}]
}

print("📡 接続テストを開始...")

res = requests.post(url, json=payload)

print(f"ステータスコード: {res.status_code}")
if res.status_code == 200:
    print("✅ 成功！Geminiの回答:")
    print(res.json()['candidates'][0]['content']['parts'][0]['text'])
else:
    print("❌ まだダメです。エラー詳細:")
    print(res.text)
