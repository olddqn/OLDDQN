import os
import tweepy
import time
from google import genai

def generate_akuh_content(language):
    # Forced use of API version 'v1' to avoid the 404/v1beta ghost
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
        # Calling the modern gateway
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
        print(f"Successfully posted: {text[:30]}...")
    except Exception as e:
        print(f"X API Error: {e}")

def main():
    print("Initiating Akuh Observation (Modern Gateway)...")
    
    # 1. Japanese Monologue
    jp = generate_akuh_content("jp")
    if jp: post_to_x(jp)
    
    time.sleep(15) # Wait to avoid rate limit
    
    # 2. English Monologue
    en = generate_akuh_content("en")
    if en: post_to_x(en)

if __name__ == "__main__":
    main()
