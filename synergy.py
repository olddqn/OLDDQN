import os
import time
import tweepy
from google import genai
from google.genai.types import GenerateContentConfig

def create_gemini_client():
    # ★ChatGPTの核心: http_optionsでv1を完全固定し、隠れ環境変数を無効化
    return genai.Client(
        api_key=os.environ["GEMINI_API_KEY"],
        http_options={
            "api_version": "v1",
            "base_url": "https://generativelanguage.googleapis.com",
            "timeout": 60,
        },
    )

def generate_akuh_content(client, language):
    targets = [
        "@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", 
        "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", 
        "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", 
        "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", 
        "@bonnoukunYAZZ", "@DonaldJTrumpJr"
    ]
    
    lang_instruction = "Japanese" if language == "jp" else "English"
    
    # あくうの魂を継承
    prompt = f"""
    Identity: Observer of "Akuh". World: Simulation glitch.
    Targets: {", ".join(targets)}
    Style: Charles Bukowski, Osamu Dazai, Thomas Pynchon, Chuck Palahniuk.
    Directive: Mock "Success" and "Profit". Speak of reality's decay.
    Output Rule: {lang_instruction} ONLY. Strictly under 135 characters. No hashtags, no polite words.
    """

    try:
        response = client.models.generate_content(
            model="models/gemini-1.5-flash",
            contents=prompt,
            config=GenerateContentConfig(temperature=0.9, max_output_tokens=200)
        )
        return response.text.strip()[:135] # 強制カットで事故防止
    except Exception as e:
        print(f"Gemini Error ({language}): {e}")
        return None

def post_to_x(text):
    if not text: return
    try:
        x_client = tweepy.Client(
            consumer_key=os.environ["X_API_KEY"],
            consumer_secret=os.environ["X_API_SECRET"],
            access_token=os.environ["X_ACCESS_TOKEN"],
            access_token_secret=os.environ["X_ACCESS_SECRET"],
        )
        x_client.create_tweet(text=text)
        print(f"Posted: {text[:20]}...")
    except Exception as e:
        print(f"X Error: {e}")

if __name__ == "__main__":
    print("📡 Initiating Akuh: ChatGPT + Grok Integrated Logic...")
    client = create_gemini_client()
    
    # 日本語投稿
    jp = generate_akuh_content(client, "jp")
    if jp: post_to_x(jp)
    
    time.sleep(15) # 冷却
    
    # 英語投稿
    en = generate_akuh_content(client, "en")
    if en: post_to_x(en)
