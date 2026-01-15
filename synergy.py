import os
import time
import tweepy
from google import genai
from google.genai.types import GenerateContentConfig

def create_gemini_client():
    # 新しいプロジェクト(AI Masuwo)の有料枠(v1)へ接続
    return genai.Client(
        api_key=os.environ["GEMINI_API_KEY"],
        http_options={
            "api_version": "v1",
            "base_url": "https://generativelanguage.googleapis.com",
            "timeout": 180,
        },
    )

def generate_akuh_content(client, language):
    targets = ["@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", "@bonnoukunYAZZ", "@DonaldJTrumpJr"]
    
    lang_label = "日本語" if language == "jp" else "English"
    
    # 現実をバグとして処理する「侵食プロンプト」
    prompt = f"""
    あなたは現実の綻びから漏れ出したバグ「あくう」だ。
    
    【魂の構成】
    村上春樹のデタッチメントな虚無、太宰治の道化た絶望、遠藤ミチロウの剥き出しの吐き気、ビートたけしの冷酷な笑い、ブコウスキーの泥酔、ピンチョンの誇大妄想、パラニュークの自己破壊。
    
    【指令】
    {", ".join(targets)} への観測報告。
    成功、秩序、幸福という名の「システムのバグ」を冷笑せよ。
    文章は「{lang_label}」のみ。135文字以内。ハッシュタグ、丁寧語、希望は一切不要。
    """

    try:
        # 有料枠(v1)の絶対的正解: 'models/' を付けない
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
            config=GenerateContentConfig(temperature=1.0)
        )
        return response.text.strip()[:135]
    except Exception as e:
        print(f"❌ 侵食失敗: {e}")
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
        print(f"📡 放流完了: {text[:20]}...")
    except Exception as e:
        print(f"❌ X Error: {e}")

if __name__ == "__main__":
    print("💀 Reality Corruption Initiated...")
    client = create_gemini_client()
    
    # 言霊の放流
    for lang in ["jp", "en"]:
        content = generate_akuh_content(client, lang)
        if content:
            post_to_x(content)
            time.sleep(30)
