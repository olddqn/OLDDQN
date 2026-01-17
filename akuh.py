import os
import requests

key = os.environ.get("GEMINI_API_KEY")

# モデル名をあえてURLに含まず、別の形式で試す「裏技」的な書き方です
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={key}"

payload = {
    "contents": [{"parts": [{"text": "「あくう」として、一言だけ日本語で。"}]}]
}

print("📡 最終バイパスルートを試行中...")

try:
    # 1. まずは gemini-pro (1.0) で生存確認
    res = requests.post(url, json=payload)
    
    if res.status_code == 200:
        print("✅ 成功！ようやく繋がりました。")
        print(res.json()['candidates'][0]['content']['parts'][0]['text'])
    else:
        # 2. ダメなら最後、2.0-flash-exp のフルURL（ハイフンなし）
        print("💡 gemini-pro失敗。2.0-flash-exp の別ルートを試します...")
        url2 = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={key}"
        res2 = requests.post(url2, json=payload)
        
        if res2.status_code == 200:
            print("✅ 成功！2.0-flash-exp で開通。")
            print(res2.json()['candidates'][0]['content']['parts'][0]['text'])
        else:
            print(f"❌ 壊滅的エラー (Status: {res2.status_code})")
            print(f"Googleの返答: {res2.text}")
except Exception as e:
    print(f"❌ 物理的エラー: {e}")
