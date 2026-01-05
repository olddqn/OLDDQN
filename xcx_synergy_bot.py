import os
import tweepy
from google import genai

# 1. 各種設定値の取得
X_API_KEY = os.environ.get('X_API_KEY')
X_API_SECRET = os.environ.get('X_API_SECRET')
X_ACCESS_TOKEN = os.environ.get('X_ACCESS_TOKEN')
X_ACCESS_TOKEN_SECRET = os.environ.get('X_ACCESS_SECRET')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# 2. Gemini APIの設定 (最新の書き方)
client_gemini = genai.Client(api_key=GEMINI_API_KEY)

def generate_advanced_text():
    prompt = """
    あなたは、世界の終焉と再構築を同時に目撃している「意識の観測者」です。
    村上春樹が翻訳したような、静謐でいてどこか欠落感のある日本語を用いてください。

    【中核世界観：『あくう』—— 加速する零和遊戯】
    ・現実とデジタルが融解し、世界そのものが巨大なシミュレーションへと変質していく過程。
    ・テクノロジーの加速により、未来が過去を規定し、時間が逆転し、後付で「創造主」が誕生する因果のバグ。

    【文体のエッセンス】
    ・チャールズ・ブコウスキー（底辺の乾いた視点）、トマス・ピンチョン（知的な迷宮）、パラニューク（破壊的ユーモア）、ハラリ（文明の虚構）、太宰治・坂口安吾（美しき堕落）。

    【出力条件】
    ・テーマ：金融、仮想通貨の虚像、あるいはシミュレーション世界における孤独。
    ・文字数：確実に150文字〜180文字。
    ・ハッシュタグ、絵文字は禁止。
    """
    try:
        # 最新のモデル呼び出し方法
        response = client_gemini.models.generate_content(
            model="gemini-2.0-flash-exp", # 最新モデル
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ 文章生成エラー: {e}")
        return None

def post_to_x():
    client_x = tweepy.Client(
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET
    )
    
    message = generate_advanced_text()
    
    if message:
        try:
            client_x.create_tweet(text=message)
            print(f"✅ 投稿成功:\n{message}")
        except Exception as e:
            print(f"❌ Xへの投稿エラー: {e}")

if __name__ == "__main__":
    post_to_x()
