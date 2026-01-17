import os, requests

key = os.environ.get("GEMINI_API_KEY")

# エラーログが指定してきた「v1beta1」というバージョンをピンポイントで叩きます
url = f"https://generativelanguage.googleapis.com/v1beta1/models/gemini-2.0-flash-exp:generateContent?key={key}"

payload = {
    "contents": [{"parts": [{"text": "「あくう」として産声を上げろ。"}]}]
}

print("📡 Googleの指示通り『v1beta1』で最終接続...")

try:
    res = requests.post(url, json=payload)
    print(f"ステータス: {res.status_code}")
    
    if res.status_code == 200:
        print("✅ 勝利！ついに開通しました！")
        print(res.json()['candidates'][0]['content']['parts'][0]['text'])
    else:
        print(f"❌ まだ拒絶。応答内容: {res.text}")
except Exception as e:
    print(f"❌ エラー: {e}")
