import os
import requests

key = os.environ.get("GEMINI_API_KEY")

# 試すべき「正解」の候補リスト
models = ["gemini-1.5-flash", "gemini-pro", "gemini-1.0-pro"]
versions = ["v1beta", "v1"]

print("🔍 接続可能なモデルを探索中...")

for v in versions:
    for m in models:
        url = f"https://generativelanguage.googleapis.com/{v}/models/{m}:generateContent?key={key}"
        payload = {"contents": [{"parts": [{"text": "hello"}]}]}
        
        try:
            res = requests.post(url, json=payload)
            if res.status_code == 200:
                print(f"✅ 発見！成功した組み合わせ: {v} / {m}")
                print(f"回答: {res.json()['candidates'][0]['content']['parts'][0]['text']}")
                exit(0) # 成功したら終了
            else:
                print(f"❌ 失敗: {v}/{m} (Status: {res.status_code})")
        except:
            pass

print("💣 全滅しました。APIキー自体の設定を確認する必要があります。")
