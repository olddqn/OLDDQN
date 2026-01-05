import os
import tweepy
from google import genai

# 1. クライアント初期化
client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_text():
    # 文学的ノイズと圧倒的孤独を強制するプロンプト
    prompt = """
    あなたは『あくう』の観測者。村上春樹訳のチャールズ・ブコウスキーのように、不機嫌で、乾いていて、静かな孤独を語れ。
    
    【エッセンス】
    トマス・ピンチョンの知的な迷宮、パラニュークの破壊的ユーモア、太宰治・坂口安吾のデカダンス。
    ユヴァル・ノア・ハラリの文明論的虚構を、システムの綻び（バグ）として描写せよ。

    【指令】
    「仮想通貨」「AI」「未来」等の陳腐な単語は死んでも使うな。
    冷めたコーヒーの膜や電気信号のノイズ、剥がれかけた安壁紙といった卑近な風景から書き始めろ。
    時間は逆行し、原因の前に結果が生まれる因果のバグを織り交ぜよ。

    【出力ルール】
    150文字〜180文字。ハッシュタグ・絵文字・感嘆符・丁寧語は禁止。
    """
    try:
        # models/ を入れないのが最新(v0.3.0+)の正解
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def post():
    client_x = tweepy.Client(
        os.environ.get('X_API_KEY'), os.environ.get('X_API_SECRET'),
        os.environ.get('X_ACCESS_TOKEN'), os.environ.get('X_ACCESS_SECRET')
    )
    msg = generate_text()
    if msg:
        try:
            client_x.create_tweet(text=msg)
            print(f"✅ SUCCESS: {msg}")
        except Exception as e:
            print(f"❌ X POST ERROR: {e}")

if __name__ == "__main__":
    post()
