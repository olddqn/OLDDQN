import os
import tweepy
import time
from google import genai

def generate_akuh_content(language):
    # 【最重要】有料プラン(Pay-as-you-go)専用の接続設定
    # 接続先を明確に 'v1' (正式版) に固定します
    client = genai.Client(
        api_key=os.environ.get('GEMINI_API_KEY'),
        http_options={'api_version': 'v1'}
    )
    
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    lang_instruction = "Japanese" if language == "jp" else "English"

    # あなたの「魂のプロンプト」
    prompt = f"""
    Identity: You are the observer of "Akuh." This world is a simulation glitch.
    Targets: {", ".join(targets)}
    Style: Charles Bukowski, Osamu Dazai, Thomas Pynchon, Chuck Palahniuk.
    Directive: Mock "Success" and "Profit". Speak of reality's decay and Harari's rotting fictions.
    Output Rule:
    - Language: {lang_instruction} ONLY.
    - Length: Strictly under 135 characters.
    - Format: Pure monologue. No hashtags, no emojis, no exclamation marks.
    """

    try:
        # 【最重要】モデル指定を 'models/gemini-1.5-flash' とフルパスで記述
        # これが有料枠で最も安定し、かつ安価（月数円）な指定方法です
        response = client.models.generate_content(
            model='models/gemini-1.5-flash',
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        # 有料枠でエラーが出る場合、詳細な理由を表示させます
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
    print("📡 Initiating Akuh Observation (Paid Tier Gateway)...")
    
    # 1. Japanese Monologue
    jp = generate_akuh_content("jp")
    if jp: post_to_x(jp)
    
    # 有料枠は制限が緩いですが、X側のスパム判定を避けるため15秒空けます
    time.sleep(15)
    
    # 2. English Monologue
    en = generate_akuh_content("en")
    if en: post_to_x(en)

if __name__ == "__main__":
    main()
