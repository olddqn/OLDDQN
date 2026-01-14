import os
import time
import tweepy
from google import genai
from google.genai.types import GenerateContentConfig

def create_gemini_client():
    # 有料枠(Pay-as-you-go)のProductionルートを完全にロック
    return genai.Client(
        api_key=os.environ["GEMINI_API_KEY"],
        http_options={
            "api_version": "v1",
            "base_url": "https://generativelanguage.googleapis.com",
            "timeout": 120, # タイムアウト対策で2分に延長
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
    
    # 【魂のブレンド】スターリン(ミチロウ)の破壊衝動 × たけしの冷笑
    prompt = f"""
    Identity: Observer of "Akuh" (Simulation glitch).
    Targets: {", ".join(targets)}
    Essence: 
    - Michiro Endo (The Stalin): Raw punk, vomit, obsession with the absolute, anti-establishment.
    - Beat Takeshi: Dry nihilism, "don't be ridiculous," mocking the seriousness of life, the smell of gunpowder and death.
    Directive: Mock "Success," "Profit," and "Order." Speak of reality as a rotting trash heap.
    Output Rule: {lang_instruction} ONLY. Strictly under 135 characters. No hashtags, no polite words.
    """

    try:
        response = client.models.generate_content(
            model="models/gemini-1.5-flash",
            contents=prompt,
            config=GenerateContentConfig(
                temperature=1.0, # 表現を尖らせるために少し上げます
                max_output_tokens=200
            )
        )
        return response.text.strip()[:135]
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
    print("📡 Akuh Awakening: Michiro x Takeshi blend...")
    client = create_gemini_client()
    
    # 日本語
    jp = generate_akuh_content(client, "jp")
    if jp: 
        post_to_x(jp)
        print(f"JP Content: {jp}")
    
    time.sleep(20) # 有料枠ですがX側の規制回避のため長めに待機
    
    # 英語
    en = generate_akuh_content(client, "en")
    if en: 
        post_to_x(en)
        print(f"EN Content: {en}")
