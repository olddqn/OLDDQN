import os
import tweepy

def post():
    # 1. 鍵の読み込み
    api_key = os.environ.get('X_API_KEY')
    api_secret = os.environ.get('X_API_SECRET')
    access_token = os.environ.get('X_ACCESS_TOKEN')
    access_secret = os.environ.get('X_ACCESS_SECRET')

    # 2. Xへの接続（認証）
    client_x = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_secret
    )
    
    # AIを使わない固定メッセージ
    msg = "Connection Test: あくうの接続テスト。これが届けば、Xとの接続は成功です。"
    
    try:
        # 3. 投稿の実行
        client_x.create_tweet(text=msg)
        print(f"✅ Xへの物理的な接続に成功しました！:\n{msg}")
    except Exception as e:
        print(f"❌ X投稿失敗: {e}")
        print("※ X側の権限設定(Read and Write)か、鍵の再発行(Regenerate)が必要です。")

if __name__ == "__main__":
    post()
