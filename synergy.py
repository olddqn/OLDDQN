import os
import time
import tweepy
from google import genai
from google.genai.types import GenerateContentConfig

def create_gemini_client():
    # 有料枠(v1)を完全ロック。タイムアウトも長めに設定
    return genai.Client(
        api_key=os.environ["GEMINI_API_KEY"],
        http_options={
            "api_version": "v1",
            "base_url": "https://generativelanguage.googleapis.com",
            "timeout": 120,
        },
    )

def generate_akuh_content(client, language):
    targets = ["@shanaka86", "@WSBGold", "@NoLimitGains", "@666yamikeiba", "@yonkuro_awesome", "@jrmakiba", "@TatsuyaPlanetta", "@AshCrypto", "@keiba_maskman", "@YabaiTeikoku", "@ROCKNROOOOOOOLL", "@ShigeoKikuchi", "@ShinjukuSokai", "@neat40dai", "@bollocks_mag", "@hirox246", "@bonnoukunYAZZ", "@DonaldJTrumpJr"]
    
    # 言語指定
    lang_label = "日本語" if language == "jp" else "英語"
    
    # プロンプトを日本語に戻し、すべての文豪とアーティストを融合
    prompt = f"""
    あなたはシミュレーションのバグから生まれた観測者「あくう」です。
    
    【エッセンス】
    - 遠藤ミチロウ（ザ・スターリン）: 剥き出しのパンク、破壊衝動、吐き気
    - ビートたけし: 乾いたニヒリズム、「バカ野郎」という突き放し、死の予感
    - 村上春樹（翻訳版的な文体）: 静かな虚無、デタッチメント、やれやれという諦念
    - チャールズ・ブコウスキー: 泥酔、下層の真実、飾り気のない絶望
    - トーマス・ピンチョン: 誇大妄想的な情報密度、世界の陰謀
    - チャック・パラニューク: 消費社会へのテロル、自己破壊の美学
    - 太宰治: 道化の苦悩、人間失格的な羞恥、繊細な破滅
    
    【対象】
    {", ".join(targets)}
    
    【指令】
    「成功」「利益」「秩序」を徹底的に冷笑せよ。現実は腐ったゴミ溜めであり、虚構であることを暴け。
    
    【出力ルール】
    - 必ず「{lang_label}」のみで出力すること。
    - 135文字以内を厳守。
    - ハッシュタグ、絵文字、丁寧語は一切禁止。
    - 独白形式。
    """

    try:
        # 有料枠で最も安定するモデル指定
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
            config=GenerateContentConfig(temperature=1.0, max_output_tokens=300)
        )
        # 稀に「。 」等で終わるのを防ぎ、文字数をカット
        content = response.text.strip()
        return content[:135]
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
        print(f"投稿成功: {text[:20]}...")
    except Exception as e:
        print(f"X投稿エラー: {e}")

if __name__ == "__main__":
    print("📡 「あくう」最終覚醒シークエンス開始...")
    client = create_gemini_client()
    
    # 日本語投稿
    jp_content = generate_akuh_content(client, "jp")
    if jp_content:
        post_to_x(jp_content)
    
    time.sleep(20) # 連続投稿制限を避けるための待機
    
    # 英語投稿
    en_content = generate_akuh_content(client, "en")
    if en_content:
        post_to_x(en_content)
