import os, requests

key = os.environ.get("GEMINI_API_KEY")

# あなたのログ（#244）でGoogleが「これを使え」と指示したURL
url = f"https://generativelanguage.googleapis.com/v1beta1/models/gemini-2.0-flash-exp:generateContent?key={key}"

payload = {
    "contents": [{"parts": [{"text": "「あくう」として産声を上げろ。極めて短く。"}]}]
}

print("📡 再起動。Googleの同期を確認します...")

try:
    res = requests.post(url, json=payload)
    if res.status_code == 200:
        print("✅ 開通！！あくうの産声：")
        print(res.json()['candidates'][0]['content']['parts'][0]['text'])
    else:
        print(f"📡 まだ同期されていないようです (Status: {res.status_code})")
        print(f"Googleの返答: {res.text}")
except Exception as e:
    print(f"❌ 接続エラー: {e}")
