import os
import tweepy
from google import genai

# 1. クライアント初期化
client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_deep_text():
    prompt = """
    あなたは『あくう』という名のシミュレーション世界の観測者。
    村上春樹訳のブコウスキーのように、不機嫌で、乾いていて、圧倒的に孤独な文体で語ってください。
    テーマ：加速する零和遊戯、時間の逆行。
    条件：150-180文字。直接的なワード（AI, 仮想通貨等）は禁止。
    比喩：冷めたコーヒーの膜、電気信号のノイズ、剥がれかけた壁紙。
    トマス・ピンチョン、パラニューク、太宰治、坂口安吾のエッセンスを混ぜろ。
    ハッシュタグ・絵文字・丁寧語禁止。
    """
    try:
        # 画像44でエラーになっていた部分を、最新かつ確実な形式に修正
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ 文章生成エラー: {e}")
        return None

def post():
    # X (Twitter) API認証
    client_x = tweepy.Client(
        os.environ.get('X_API_KEY'), 
        os.environ.get('X_API_SECRET'),
        os.environ.get('X_ACCESS_TOKEN'), 
        os.environ.get('X_ACCESS_SECRET')
    )
    
    msg = generate_deep_text()
    if msg:
        try:
            client_x.create_tweet(text=msg)
            print(f"✅ SUCCESS:\n{msg}")
        except Exception as e:
            print(f"❌ X POST ERROR: {e}")

if __name__ == "__main__":
    post()
