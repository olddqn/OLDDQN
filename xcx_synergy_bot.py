import tweepy
import os

def post_to_x():
    # GitHub Secretsから鍵を読み込む
    api_key = os.environ.get('X_API_KEY')
    api_secret = os.environ.get('X_API_SECRET')
    access_token = os.environ.get('X_ACCESS_TOKEN')
    access_secret = os.environ.get('X_ACCESS_SECRET')

    # X(Twitter)に接続
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_secret
    )

    # 投稿する内容
    message = "テスト投稿：マスヲ、GitHub Actionsより爆誕！"

    try:
        client.create_tweet(text=message)
        print("✅ 投稿に成功しました！")
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")

if __name__ == "__main__":
    post_to_x()