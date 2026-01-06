import os
import tweepy
from google import genai

# 1. Geminiの初期化
client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_deep_text():
    prompt = """
    あなたは『あくう』という名のシミュレーション世界の観測者。
    村上春樹訳のチャールズ・ブコウスキーのように、不機嫌で、乾いていて、圧倒的に孤独な文体で語ってください。
    150-180文字。ハッシュタグ・絵文字・丁寧語禁止。
    テーマ：冷めたコーヒーの膜、電気信号のノイズ、剥がれかけた壁紙。
    """
    try:
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ 文章生成エラー: {e}")
        return None

def post():
    # 2. X (Twitter) API認証（最新の権限付き鍵を使用）
    # GitHubのSecretsに登録した鍵を環境変数から読み込みます
    api_key = os.environ.get('X_API_KEY')
    api_secret = os.environ.get('X_API_SECRET')
    access_token = os.environ.get('X_ACCESS_TOKEN')
    access_secret = os.environ.get('X_ACCESS_SECRET')

    client_x = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_secret
    )
    
    msg = generate_deep_text()
    if msg:
        try:
            # ここで実際にXのタイムラインに書き込みます
            client_x.create_tweet(text=msg)
            print(f"✅ 成功！Xに投稿されました:\n{msg}")
        except Exception as e:
            print(f"❌ X投稿失敗: {e}")
            print("※ 権限変更後の『再発行（Regenerate）』した鍵がGitHubに登録されているか確認してください。")

if __name__ == "__main__":
    post()
