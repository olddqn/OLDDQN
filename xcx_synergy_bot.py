import os
import tweepy
import random

# GitHubのSecretsから値を取得
API_KEY = os.environ.get('X_API_KEY')
API_SECRET = os.environ.get('X_API_SECRET')
ACCESS_TOKEN = os.environ.get('X_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('X_ACCESS_SECRET')

def get_twitter_client():
    # 修正した変数名を使って認証します
    return tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

# ここから下の「def masuwo_bukowski_action():」などはそのまま残す

def masuwo_bukowski_action():
    client = get_twitter_client()
    
    messages = [
        "世界を救おうなんて連中は、自分の靴紐の結び方すら知らねえ。俺はただ、ビットコインが死んでいくのを眺めてる。 #Bukowski #Crypto",
        "天才になるには時間がかかるが、クズになるのは一瞬だ。アニメのヒロインが画面で泣いている。俺は安酒を飲み、この馬鹿げた世界に乾杯するよ。",
        "陰謀論？ 結構なことだ。だが現実はそれよりずっと退屈で残酷だ。どぶのネズミの方が、メタバースで踊る奴らよりマシな顔をしてやがる。",
        "パンクってのは、他人のルールで踊らないことだ。たとえそこが地獄の底でもな。漫画を読み耽り、夜が明けるのを待つ。それが俺の聖書だ。",
        "政府も神も、俺の家賃を払っちゃくれない。暗号資産の暴落を笑い飛ばせ。人生なんてのは、負け続けることを学ぶための長いレースなんだよ。"
    ]
    
    try:
        client.create_tweet(text=random.choice(messages))
        print("✅ 投稿完了")
    except Exception as e:
        print(f"❌ 投稿エラー: {e}")

    keywords = ['ビットコイン', 'アンダーグラウンド', 'サイバーパンク', '都市伝説', '深夜アニメ', 'ディストピア']
    target_word = random.choice(keywords)
    
    try:
        query = f'{target_word} -is:retweet' 
        tweets = client.search_recent_tweets(query=query, max_results=5)
        if tweets.data:
            for tweet in tweets.data:
                client.like(tweet.id)
                client.follow_user(tweet.author_id)
                print(f"👍 {target_word} へのアクション完了")
    except Exception as e:
        print(f"❌ アクションエラー: {e}")

if __name__ == "__main__":
    masuwo_bukowski_action()
