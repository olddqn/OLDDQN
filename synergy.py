import os
import tweepy
from google import genai

# 1. クライアント初期化 (Gemini)
client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_deep_text():
    prompt = """
    あなたは『あくう』の観測者。村上春樹訳のブコウスキーのように、不機嫌で、静かで、圧倒的に孤独な文体で語ってください。
    150-180文字。ハッシュタグ・絵文字・丁寧語は禁止。
    テーマ：冷めたコーヒー、剥がれかけた壁紙、電気信号のノイズ。
    """
    try:
        # 画像51で修正された最新形式
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ 文章生成失敗: {e}")
        return None

def post():
    # 環境変数から鍵を取得
    api_key = os.environ.get('X_API_KEY')
    api_secret = os.environ.get('X_API_SECRET')
    access_token = os.environ.get('X_ACCESS_TOKEN')
    access_secret = os.environ.get('X_ACCESS_SECRET')

    # 鍵が空っぽでないかチェック
    if not all([api_key, api_secret, access_token, access_secret]):
        print("❌ エラー: XのAPIキーがGitHubのSettingsで設定されていない可能性があります。")
        return

    # X (Twitter) API認証
    client_x = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_secret
    )
    
    msg = generate_deep_text()
    if msg:
        try:
            client_x.create_tweet(text=msg)
            print(f"✅ 投稿成功:\n{msg}")
        except Exception as e:
            print(f"❌ X投稿エラー詳細: {e}")
            print("※ 鍵（Secrets）が正しいか、Xのアプリに投稿権限(Read and Write)があるか確認してください。")

if __name__ == "__main__":
    post()
