import os
import tweepy
import google.generativeai as genai

# 1. 各種設定値の取得
X_API_KEY = os.environ.get('X_API_KEY')
X_API_SECRET = os.environ.get('X_API_SECRET')
X_ACCESS_TOKEN = os.environ.get('X_ACCESS_TOKEN')
X_ACCESS_TOKEN_SECRET = os.environ.get('X_ACCESS_SECRET')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# 2. Gemini APIの設定（最新のモデル指定に変更）
genai.configure(api_key=GEMINI_API_KEY)
# 最も互換性の高い 'gemini-1.5-flash-latest' を使用します
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def generate_advanced_text():
    prompt = """
    あなたは、世界の終焉と再構築を同時に目撃している「意識の観測者」です。
    村上春樹が翻訳したような、静謐でいてどこか欠落感のある日本語を用いてください。

    【中核世界観：『あくう』—— 加速する零和遊戯】
    ・現実とデジタルが融解し、世界そのものが巨大なシミュレーションへと変質していく。
    ・テクノロジーの加速により、未来が過去を規定し、時間が逆転し、後付で「創造主」が誕生する因果のバグ。
    ・すべてはゼロに収束するが、その収束速度だけが無限に加速していく虚無。

    【文体のエッセンス】
    ・ベース：チャールズ・ブコウスキー（底辺の乾いた視点、安酒、諦念）
    ・構成：トマス・ピンチョン、ボードリヤール（情報理論的迷宮、シミュラークルの暴走）
    ・過激：パラニューク、アーヴィン・ウェルシュ（破壊的ユーモア、システムのバグ）
    ・哲学：ユヴァル・ノア・ハラリ（文明の虚構）、太宰治・坂口安吾（美しき堕落）

    【出力条件】
    ・テーマ：金融、仮想通貨の虚像、あるいはシミュレーション世界における孤独について。
    ・文字数：確実に150文字〜180文字。
    ・ハッシュタグ、絵文字、お仕着せの格言は一切禁止。
    """
    try:
        response = model.generate_content(prompt)
        # 生成されたテキストが空でないか確認
        if response and response.text:
            return response.text.strip()
        else:
            print("❌ 文章が空で生成されました")
            return None
    except Exception as e:
        print(f"❌ 文章生成エラーの詳細: {e}")
        return None

def post_to_x():
    client = tweepy.Client(
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET
    )
    
    message = generate_advanced_text()
    
    if message:
        try:
            client.create_tweet(text=message)
            print(f"✅ 投稿成功:\n{message}")
        except Exception as e:
            print(f"❌ Xへの投稿エラー: {e}")
    else:
        print("❌ メッセージ生成に失敗したため投稿を中断しました")

if __name__ == "__main__":
    post_to_x()
