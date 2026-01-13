import os
import tweepy
import google.generativeai as genai
import time

# Configure Gemini API
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_akuh_content(language):
    # Observation Targets
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]

    # Language specific instruction
    lang_instruction = "Japanese" if language == "jp" else "English"

    # The Core Identity Prompt
    prompt = f"""
    Identity: You are the observer of "Akuh." This world is a simulation glitch.
    Targets: {", ".join(targets)}
    Style: Charles Bukowski, Osamu Dazai, Thomas Pynchon, Chuck Palahniuk.
    Directive: Mock "Success" and "Profit". Speak of reality's decay and Harari's rotting fictions.

    Output Rule:
    - Language: {lang_instruction} ONLY.
    - Length: Strictly under 135 characters.
    - Format: Pure monologue. No hashtags, no emojis, no exclamation marks, no polite language.
    """

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API Error ({language}): {e}")
        return None

def post_to_x(text):
    if not text:
        return
    try:
        client = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        client.create_tweet(text=text)
        print(f"Successfully posted: {text[:30]}...")
    except Exception as e:
        print(f"X API Error: {e}")

def main():
    print("Initiating Akuh Simulation Observation (Dual Language Mode)...")
    
    # 1. Generate and Post Japanese Version
    jp_content = generate_akuh_content("jp")
    if jp_content:
        post_to_x(jp_content)
    
    # Wait a bit to avoid API spam detection
    time.sleep(10)
    
    # 2. Generate and Post English Version
    en_content = generate_akuh_content("en")
    if en_content:
        post_to_x(en_content)

if __name__ == "__main__":
    main()
