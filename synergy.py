import os
import tweepy
from google import genai

# 1. Gemini クライアント初期化
try:
    client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
except Exception as e:
    print(f"❌ Gemini初期化エラー: {e}")

def generate_deep_text():
    prompt = """
    あなたは『あくう』の観測者。村上春樹訳のブコウスキーのように、不機嫌で、静かで、圧倒的に孤独な文体で語れ。
    150-180文字。ハッシュタグ・絵文字・丁寧語禁止。
    テーマ：冷めたコーヒーの膜、電気信号のノイズ、剥がれかけた壁紙。
    """
    try:
        # 最新の書き方
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ 文章生成失敗: {e}")
        return None

def post():
    # 環境変数（Secrets）の取得
    keys = {
        "CK": os.environ.get('X_API_KEY'),
        "CS": os.environ.get('X_API_SECRET'),
        "AT": os.environ.get('X_ACCESS_TOKEN'),
        "AS": os.environ.get('X_ACCESS_SECRET')
    }

    # 鍵のチェック
    for name, value in keys.items():
        if not value:
            print(f"❌ エラー: {name} が設定されていません。GitHubのSettingsを確認してください。")
            return

    try:
        # X (Twitter) 認証
        client_x = tweepy.Client(
            consumer_key=keys["CK"],
            consumer_secret=keys["CS"],
            access_token=keys["AT"],
            access_token_secret=keys["AS"]
        )
        
        msg = generate_deep_text()
        if msg:
            client_x.create_tweet(text=msg)
            print(f"✅ 成功しました:\n{msg}")
    except Exception as e:
        print(f"❌ X投稿エラー詳細: {e}")
        print("💡 ヒント: X Developer PortalでAppの権限が 'Read and Write' になっているか確認してください。")

if __name__ == "__main__":
    post()
