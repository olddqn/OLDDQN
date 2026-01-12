import os
import tweepy
import google.generativeai as genai
import random

# Gemini設定
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def main():
    # 1. X API クライアント設定 (v2 + v1.1 併用)
    auth = tweepy.OAuthHandler(os.environ.get('X_API_KEY'), os.environ.get('X_API_SECRET'))
    auth.set_access_token(os.environ.get('X_ACCESS_TOKEN'), os.environ.get('X_ACCESS_SECRET'))
    api_v1 = tweepy.API(auth)
    
    client_v2 = tweepy.Client(
        consumer_key=os.environ.get('X_API_KEY'),
        consumer_secret=os.environ.get('X_API_SECRET'),
        access_token=os.environ.get('X_ACCESS_TOKEN'),
        access_token_secret=os.environ.get('X_ACCESS_SECRET')
    )

    targets = ["@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", "@bonnoukunYAZZ", "@DonaldJTrumpJr"]

    try:
        # --- Geminiで独白を生成 ---
        # 当時最も安定していた指定方法
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"あなたは『あくう』。以下のノイズを観測せよ：{', '.join(targets)}。130文字以内で冷笑的な独白を出力せよ。"
        
        response = model.generate_content(prompt)
        msg = response.text.strip()
        
        # --- Xに投稿 ---
        client_v2.create_tweet(text=msg)
        print(f"✅ 独白投稿成功: {msg}")

        # --- 自動いいね・フォロー巡回 ---
        target_user = random.choice(targets).replace("@", "")
        print(f"🔍 ターゲット {target_user} を巡回中...")
        
        # 最新ツイートを取得していいね
        user_tweets = client_v2.get_users_tweets(id=client_v2.get_user(username=target_user).data.id, max_results=5)
        if user_tweets.data:
            tweet_id = user_tweets.data[0].id
            client_v2.like(tweet_id)
            print(f"💖 Tweet {tweet_id} にいいねしました")

    except Exception as e:
        print(f"❌ エラー発生: {e}")
        # 403が出る場合、ここで詳細がわかります
        raise e

if __name__ == "__main__":
    main()
