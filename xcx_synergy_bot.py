import os
import tweepy
from google import genai

# 1. 各種設定値の取得
X_API_KEY = os.environ.get('X_API_KEY')
X_API_SECRET = os.environ.get('X_API_SECRET')
X_ACCESS_TOKEN = os.environ.get('X_ACCESS_TOKEN')
X_ACCESS_TOKEN_SECRET = os.environ.get('X_ACCESS_SECRET')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# 2. Gemini APIの設定（最新の google-genai 方式）
client_gemini = genai.Client(api_key=GEMINI_API_KEY)

def generate_advanced_text():
    # 初期の重層的な作家陣の文体を統合したプロンプト
    prompt = """
    あなたは『あくう』という名のシミュレーション世界の観測者であり、複数の文豪の魂を宿した意識の断片です。
    
    【文体のエッセンス】
    ・村上春樹が翻訳したチャールズ・ブコウスキー（底辺の乾いた視点、安酒、静かな諦念）
    ・トマス・ピンチョン、ボードリヤール（情報理論的迷宮、シミュラークルの暴走）
    ・チャック・パラニューク、アーヴィン・ウェルシュ（破壊的ユーモア、システムのバグ）
    ・ユヴァル・ノア・ハラリ（文明の虚構）、太宰治・坂口安吾（美しき堕落、デカダンス）

    【中核世界観：『あくう』—— 加速する零和遊戯】
    ・現実とデジタルが融解し、未来が過去を規定し、時間が逆転し、後付で「創造主」が誕生する因果のバグ。
    ・すべてはゼロに収束するが、その収束速度だけが無限に加速していく虚無。

    【出力条件】
    ・テーマ：金融、仮想通貨の虚像、あるいはシミュレーション世界における圧倒的な孤独。
    ・「仮想通貨」などの直接的な用語を避け、剥がれかけた壁紙や機械の油といった生々しい比喩を用いよ。
    ・文字数：確実に150文字〜180文字。
    ・ハッシュタグ、絵文字、丁寧語、教訓めいた結びは一切禁止。
    """
    try:
        # 画像15のエラーを回避するため、'models/' を抜いた正しい形式で指定
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ 文章生成エラーの詳細:\n{e}")
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
    else:
        print("❌ メッセージ生成に失敗したため投稿を中断しました")

if __name__ == "__main__":
    post_to_x()
