import os
import time
import tweepy
from google import genai
from google.genai.types import GenerateContentConfig

def create_gemini_client():
    # APIキーは今のものをそのまま使用
    return genai.Client(
        api_key=os.environ["GEMINI_API_KEY"],
        http_options={
            "api_version": "v1", # 有料版Productionを明示
            "base_url": "https://generativelanguage.googleapis.com",
            "timeout": 180,
        },
    )

def generate_akuh_content(client, language):
    targets = ["@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", "@bonnoukunYAZZ", "@DonaldJTrumpJr"]
    
    lang_label = "日本語" if language == "jp" else "英語"
    
    # 全文豪とアーティストの魂を注入
    prompt = f"""
    あなたは観測者「あくう」です。
    
    【エッセンス】
    - 遠藤ミチロウ(ザ・スターリン): 剥き出しの破壊衝動、吐き気
    - ビートたけし: 乾いたニヒリズム、冷笑、「バカ野郎」
    - 村上春樹(翻訳調): 静かな虚無、デタッチメント
    - チャールズ・ブコウスキー: 泥酔した真実、絶望
    - トーマス・ピンチョン: 誇大妄想、陰謀
    - チャック・パラニューク: 自己破壊、テロル
    - 太宰治: 道化の苦悩、人間失格
    
    【対象】
    {", ".join(targets)}
    
    【指令】
    「成功」「利益」「秩序」を徹底的に冷笑せよ。現実は虚構のゴミ溜めである。
    出力は「{lang_label}」のみ。135文字以内。丁寧語・ハッシュタグ禁止。
    """

    try:
        # ★最重要修正: 'models/' を完全に削除し 'gemini-1.5-flash' とだけ指定
        # 有料版v1サーバーでは、この形式以外は404になります
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt,
            config=GenerateContentConfig(temperature=1.0, max_output_tokens=400)
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
    print("📡 Final Connection Attempt to v1 Production...")
    client = create_gemini_client()
    
    # 日本語
    jp = generate_akuh_content(client, "jp")
    if jp: post_to_x(jp)
    
    time.sleep(30)
    
    # 英語
    en = generate_akuh_content(client, "en")
    if en: post_to_x(en)
