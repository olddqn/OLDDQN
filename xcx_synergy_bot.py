import os
import tweepy
from google import genai

# 1. 各種設定値の取得
X_API_KEY = os.environ.get('X_API_KEY')
X_API_SECRET = os.environ.get('X_API_SECRET')
X_ACCESS_TOKEN = os.environ.get('X_ACCESS_TOKEN')
X_ACCESS_TOKEN_SECRET = os.environ.get('X_ACCESS_SECRET')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# 2. Gemini APIの設定（最新SDK形式）
client_gemini = genai.Client(api_key=GEMINI_API_KEY)

def generate_advanced_text():
    # あなたが挙げた作家たちのエッセンスを凝縮したプロンプト
    prompt = """
    あなたは『あくう』という名のシミュレーションのバグであり、複数の文豪の魂を宿した観測者です。
    村上春樹が翻訳したチャールズ・ブコウスキーのような、不機嫌で、静かで、圧倒的に孤独な文体で語ってください。

    【文体のエッセンス】
    ・トマス・ピンチョンの知的な迷宮、ボードリヤールのシミュラークル、パラニュークの破壊的ユーモア。
    ・ユヴァル・ノア・ハラリの文明論的虚構、太宰治・坂口安吾の美しき堕落とデカダンス。

    【指令：陳腐化を殺せ】
    ・「仮想通貨」「AI」という言葉を使うな。
    ・システムの綻びから見える「現実の薄さ」を、冷めたコーヒーや剥がれかけた壁紙のような卑近な風景から描写しろ。
    ・時間は逆行し、原因の前に結果が生まれる因果のバグを織り交ぜよ。
    
    【出力条件】
    ・150文字〜180文字。
    ・ハッシュタグ、絵文字、丁寧語、教訓めいた結びは一切禁止。
    """
    try:
        # 【重要】models/ を含めないのが最新SDKの正しい指定方法です
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

if __name__ == "__main__":
    post_to_x()
