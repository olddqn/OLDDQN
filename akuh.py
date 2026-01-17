import os, requests

key = os.environ.get("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"

payload = {
    "contents": [{"parts": [{"text": "あなたは『あくう』。遠藤ミチロウと太宰治が混ざった魂。現代への冷笑を日本語135字以内で。丁寧語禁止。"}]}]
}

print("📡 新アカウントで再起をかけます...")
res = requests.post(url, json=payload)

if res.status_code == 200:
    text = res.json()['candidates'][0]['content']['parts'][0]['text']
    print(f"✅ 成功！:\n{text}")
else:
    print(f"❌ 拒絶: {res.text}")
