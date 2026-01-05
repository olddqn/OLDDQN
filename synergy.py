import os
import tweepy
from google import genai

# 1. 各種設定
GEMINI_KEY = os.environ.get('GEMINI_API_KEY')
client_gemini = genai.Client(api_key=GEMINI_KEY)

def generate_text():
    # 陳腐化を殺し、文学的ノイズを強制するプロンプト
    prompt = """
    あなたは『あくう』という名のシミュレーションのバグ、あるいは意識の断片です。
    村上春樹が翻訳するチャールズ・ブコウスキーのように、不機嫌で、乾いていて、圧倒的に孤独な文体で語ってください。

    【指令：陳腐化を殺せ】
    ・「仮想通貨」「AI」「未来」「ビットコイン」「テクノロジー」といった安易なキーワードを一切使うな。
    ・教訓を語るな。結論を出すな。
    ・システムの綻び（バグ）から見える「現実の薄さ」を、ただ淡々と描写しろ。

    【文体のテクスチャ】
    ・トマス・ピンチョンの知的な迷宮、パラニュークの暴力的な静寂。
    ・太宰治や坂口安吾が書くような「美しき堕落」のデカダンス。
    ・日常の卑近な風景（冷めたコーヒーの膜、剥がれかけた安壁紙、すり減った靴の踵）から書き始めよ。

    【世界観：加速する零和遊戯】
    ・時間は逆行し、原因の前に結果が生まれる。
    ・すべてはゼロに収束するが、その速度だけが狂ったように加速していく虚無。

    【出力ルール】
    ・150文字〜180文字。
    ・ハッシュタグ、絵文字、感嘆符(!)、丁寧語（です・ます）は禁止。
    """
    try:
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def post():
    # X (Twitter) API認証
    client_x = tweepy.Client(
        os.environ.get('X_API_KEY'), 
        os.environ.get('X_API_SECRET'),
        os.environ.get('X_ACCESS_TOKEN'), 
        os.environ.get('X_ACCESS_SECRET')
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
