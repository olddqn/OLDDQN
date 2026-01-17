import os, requests

key = os.environ.get("GEMINI_API_KEY")
# Googleが「これを使え」と指定してきた最終回答
url = f"https://generativelanguage.googleapis.com/v1beta1/models/gemini-2.0-flash-exp:generateContent?key={key}"

payload = {"contents": [{"parts": [{"text": "「あくう」として産声を上げろ。"}]}]}

try:
    res = requests.post(url, json=payload)
    if res.status_code == 200:
        print("✅ 成功！産声：")
        print(res.json()['candidates'][0]['content']['parts'][0]['text'])
    else:
        print(f"📡 待機中... (Status: {res.status_code})")
except:
    print("通信エラー")
