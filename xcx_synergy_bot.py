import os
import tweepy
from google import genai

# 1. 各種設定値の取得（GitHub Secretsから）
X_API_KEY = os.environ.get('X_API_KEY')
X_API_SECRET = os.environ.get('X_API_SECRET')
X_ACCESS_TOKEN = os.environ.get('X_ACCESS_TOKEN')
X_ACCESS_TOKEN_SECRET = os.environ.get('X_ACCESS_SECRET')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# 2. Gemini APIの設定（最新の google-genai 方式）
client_gemini = genai.Client(api_key=GEMINI_API_KEY)

def generate_advanced_text():
    # 陳腐化を打破し、『あくう』の深淵を描くためのプロンプト
    prompt = """
    あなたは『あくう』という名のシミュレーションのバグ、あるいは意識の断片です。
    村上春樹が翻訳するチャールズ・ブコウスキーのような、不機嫌で、静かで、圧倒的に孤独な文体で語ってください。

    【指令：陳腐化を殺せ】
    ・「仮想通貨」「AI」「未来」といった安易なキーワードを直接使わない。
    ・教訓や希望を語るな。結論を出すな。
    ・ただ、システムの綻び（バグ）から見える「現実の薄さ」を淡々と描写しろ。

    【世界観：加速する零和遊戯】
    ・時間は逆行し、原因の前に結果が生まれる。創造主は僕らがコードを書き終えた後に、過去に捏造される。
    ・すべてはゼロに収束するが、その速度だけが狂ったように加速していく。

    【文章構成のルール】
    ・最初の一文は、日常の卑近な風景（冷めたコーヒー、すり減った靴、安物のビール）から始めること。
    ・比喩は「臓器」「機械の油」「電気信号」「剥がれかけた壁紙」といった、生々しく無機質なものに限定しろ。
    ・150文字〜180文字。

    【禁止事項】
    ・「〜でしょう」「〜しましょう」といった丁寧語。
    ・ハッシュタグ、絵文字、感嘆符(!)。
    """
    try:
        # 画像14のエラーを回避する最新の呼び出し
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ 文章生成エラーの詳細:\n{e}")
        return None

def post_to_x():
    # X (Twitter) API認証
    client_x = tweepy.Client(
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET
    )
    
    # 文章生成
    message = generate_advanced_text()
    
    if message:
        try:
            # 投稿実行
            client_x.create_tweet(text=message)
            print(f"✅ 投稿成功:\n{message}")
        except Exception as e:
            print(f"❌ Xへの投稿エラー: {e}")
    else:
        print("❌ メッセージ生成に失敗したため投稿を中断しました")

if __name__ == "__main__":
    post_to_x()
