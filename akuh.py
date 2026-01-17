import os, requests

key = os.environ.get("GEMINI_API_KEY")

# 1. 今使えるモデルの一覧をGoogleに聞き出す
list_url = f"https://generativelanguage.googleapis.com/v1/models?key={key}"

print("📡 利用可能なモデルをリストアップします...")

try:
    res = requests.get(list_url)
    models_data = res.json()
    
    if "models" in models_data:
        available_models = [m["name"] for m in models_data["models"]]
        print(f"✅ 発見！あなたが今使えるモデル一覧:\n{available_models}")
        
        # 2. その中から一番強そうなやつを自動で選んでテスト
        target = ""
        for m in ["models/gemini-1.5-flash", "models/gemini-1.0-pro", "models/gemini-pro"]:
            if m in available_models:
                target = m
                break
        
        if target:
            print(f"🚀 {target} で接続テストします...")
            test_url = f"https://generativelanguage.googleapis.com/v1/{target}:generateContent?key={key}"
            payload = {"contents": [{"parts": [{"text": "hello"}]}]}
            test_res = requests.post(test_url, json=payload)
            print(f"結果: {test_res.status_code}")
            if test_res.status_code == 200:
                print(f"回答: {test_res.json()['candidates'][0]['content']['parts'][0]['text']}")
        else:
            print("❌ 適切なモデルが見つかりませんでした。")
    else:
        print(f"❌ モデル一覧が取れませんでした: {models_data}")
except Exception as e:
    print(f"❌ 通信エラー: {e}")
