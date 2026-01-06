import os
import tweepy

def post():
    # GitHubのSecretsから鍵を読み込む
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
    
    # AIを使わず、固定のテストメッセージ
    msg = "Connection Test: あくうの接続テスト。これが届けば、道は開ける。"
    
    try:
        client_x.create_tweet(text=msg)
        print(f"✅ 物理的な接続に成功しました！:\n{msg}")
    except Exception as e:
        print(f"❌ X投稿失敗（まだ接続に問題があります）: {e}")

if __name__ == "__main__":
    post()
