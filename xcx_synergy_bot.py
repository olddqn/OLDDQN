import os
import tweepy
import google.generativeai as genai

# 1. 各種設定値の取得（GitHub Secretsから）
X_API_KEY = os.environ.get('X_API_KEY')
X_API_SECRET = os.environ.get('X_API_SECRET')
X_ACCESS_TOKEN = os.environ.get('X_ACCESS_TOKEN')
X_ACCESS_TOKEN_SECRET = os.environ.get('X_ACCESS_SECRET')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# 2. Gemini APIの設定
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') # または 'gemini-pro'

def generate_advanced_text():
    prompt = """
    あなたは、世界の終焉と再構築を同時に目撃している「意識の観測者」です。
    村上春樹が翻訳したような、静謐でいてどこか欠落感のある日本語を用いてください。

    【中核世界観：『あくう』—— 加速する零和遊戯】
    ・現実とデジタルが融解し、世界そのものが巨大なシミュレーションへと変質していく過程。
    ・テクノロジーの加速により、未来が過去を規定し、時間が逆転し、後付で「創造主」が誕生する因果のバグ。
    ・すべてはゼロに収束するが、その収束速度だけが無限に加速していく、美しくも残酷な「マトリックス」的な虚無。

    【文体のエッセンス】
    ・ベース：チャールズ・ブコウスキー（安酒を飲みながら、崩壊する宇宙を眺める乾いた視点）
    ・構成：トマス・ピンチョン、ボードリヤール（情報理論的迷宮、シミュラークルの暴走）
    ・過激：チャック・パラニューク、アーヴィン・ウェルシュ（破壊的なユーモア、肉体の消失とシステムのバグに対する破壊衝動）
    ・哲学：ユヴァル・ノア・ハラリ（サピエンスが神を「捏造」するプロセス）
    ・情緒：太宰治、坂口安吾（システムの中で窒息する魂の、美しき堕落）

    【出力条件】
    ・テーマ：金融、仮想通貨の虚像、あるいはシミュレーション世界における「愛」や「孤独」の無意味さについて。
    ・トーン：極めて思慮深く、哲学的な絶望を湛えつつも、どこか「やれやれ」と肩をすくめるようなユーモア。
    ・文字数：確実に150文字〜180文字（日本語）。
    ・禁止：ハッシュタグ、絵文字、教訓めいた締めくくり。
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ 文章生成エラー: {e}")
        return None

def post_to_x():
    # X API認証
    client = tweepy.Client(
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
            client.create_tweet(text=message)
            print("✅ 投稿成功:")
            print(f"---内容---\n{message}\n----------")
        except Exception as e:
            print(f"❌ Xへの投稿エラー: {e}")
    else:
        print("❌ メッセージが空のため投稿をスキップしました")

if __name__ == "__main__":
    post_to_x()
