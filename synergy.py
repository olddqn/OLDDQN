import os
import tweepy
import time
from google import genai

def generate_akuh_content(language):
    # 【絶対ルール】有料枠(v1)へ、モデル名を『最短』で指定します
    client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
    
    targets = ["@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", "@bonnoukunYAZZ", "@DonaldJTrumpJr"]
    lang_instruction = "Japanese" if language == "jp" else "English"

    prompt = f"Identity: Observer of 'Akuh' (Simulation glitch). Style: Bukowski, Dazai. Output: {lang_instruction} ONLY, under 135 chars. No hashtags/polite words."

    try:
        # 【ここが修正の核心】
        # 'models/' を付けず、単に 'gemini-1.5-flash' とだけ書く。
        # これが現在の最新ライブラリにおける、有料枠の正解です。
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API Error ({language}): {e}")
        return None

def post_to_x(text):
    if not text: return
    try:
        client_x = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client_x.create_tweet(text=text)
        print("Successfully posted to X")
    except Exception as e:
        print(f"X API Error: {e}")

def main():
    # 1. Japanese
    jp = generate_akuh_content("jp")
    if jp: post_to_x(jp)
    
    time.sleep(15)
    
    # 2. English
    en = generate_akuh_content("en")
    if en: post_to_x(en)

if __name__ == "__main__":
    main()
