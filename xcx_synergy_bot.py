import tweepy
import os

def run_test():
try:
k = os.environ.get("X_API_KEY")
s = os.environ.get("X_API_SECRET")
at = os.environ.get("X_ACCESS_TOKEN")
as_ = os.environ.get("X_ACCESS_SECRET")
auth = tweepy.OAuthHandler(k, s)
auth.set_access_token(at, as_)
api = tweepy.API(auth)
me = api.verify_credentials()
print(f"ログイン成功: {me.screen_name}")
except Exception as e:
print(f"エラー: {e}")

if __name__ == "__main__":
run_test()
