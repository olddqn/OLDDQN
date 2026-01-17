import os
import tweepy

def post_to_x(text: str):
    try:
        client = tweepy.Client(
            consumer_key=os.environ["X_API_KEY"],
            consumer_secret=os.environ["X_API_SECRET"],
            access_token=os.environ["X_ACCESS_TOKEN"],
            access_token_secret=os.environ["X_ACCESS_SECRET"],
        )
        client.create_tweet(text=text)
        print("Xへの投稿に成功しました。")
    except Exception as e:
        print(f"X投稿エラー: {e}")
