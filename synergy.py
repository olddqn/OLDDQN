import os
import tweepy

def post():
    # 4つの鍵をすべて個別に読み込む
    consumer_key = os.environ.get('X_API_KEY')
    consumer_secret = os.environ.get('X_API_SECRET')
    access_token = os.environ.get('X_ACCESS_TOKEN')
    access_token_secret = os.environ.get('X_ACCESS_SECRET')

    # v1.1とv2の両方の認証を組み合わせた、最も確実な認証方式
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api_v1 = tweepy.API(auth)
    
    # 投稿にはv2のClientを使用
    client_v2 = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )
    
    msg = "Physical Connection Test: 認証方式を変更して再テスト。これが最後のエラー確認です。"
    
    try:
        # v2での投稿
        client_v2.create_tweet(text=msg)
        print(f"✅ ついに投稿成功:\n{msg}")
    except Exception as e:
        print(f"❌ まだエラーが出ます: {e}")
        # ここで「認証エラー」か「権限エラー」か「プラン制限」かを表示します
        if "403" in str(e):
            print("💡 403エラー: X側の『App設定』の中のApp TypeやCallback URLが未設定の可能性があります。")

if __name__ == "__main__":
    post()
