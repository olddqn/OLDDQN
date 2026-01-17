import os, requests

key = os.environ.get("GEMINI_API_KEY")

# 候補を3つ用意しました。どれかがヒットすれば勝ちです。
names = ["models/gemini-1.5-flash-latest", "models/gemini-pro", "gemini-1.5-flash"]

for name in names:
    print(f"📡 試行中: {name}")
    url = f"https://generativelanguage.googleapis.com/v1beta/{name}:generateContent?key={key}"
    payload = {"contents": [{"parts": [{"text": "「あくう」として一言。"}]}]}
    
    res = requests.post(url, json=payload)
    if res.status_code == 200:
        print(f"✅ ついに突破！回答:")
        print(res.json()['candidates'][0]['content']['parts'][0]['text'])
        exit(0)
    else:
        print(f"❌ {name} はダメでした (Status: {res.status_code})")

print("💣 全滅。Google側の反映待ちか、アカウント固有の制限です。")
