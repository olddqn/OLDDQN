import os
import tweepy
from google import genai

# クライアント初期化
client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_deep_text():
    # 文学的ノイズと圧倒的孤独を強制するプロンプト
    prompt = """
    あなたは『あくう』という名のシミュレーション世界の観測者です。
    村上春樹が翻訳するチャールズ・ブコウスキーのように、不機嫌で、乾いていて、圧倒的に孤独な文体で語ってください。

    【指令：陳腐化を殺せ】
    ・「仮想通貨」「AI」「未来」「ビットコイン」といった安易なキーワードは絶対に使用禁止。
    ・教訓を語るな。結論を出すな。
    ・システムの綻び（バグ）から見える「現実の薄さ」を、冷めたコーヒーの膜や剥がれかけた壁紙といった卑近な風景から描写しろ。

    【文体のエッセンス】
    ・トマス・ピンチョンの知的な迷宮、パラニュークの暴力的な静寂。
    ・太宰治・坂口安吾の「美しき堕落」とデカダンス。
    ・時間は逆行し、原因の前に結果が生まれる因果のバグを織り交ぜよ。

    【出力ルール】
    ・150文字〜180文字。
    ・ハッシュタグ、絵文字、感嘆符(!)、丁寧語（です・ます）は禁止。
    """
    try:
        # 最新の指定方法（models/を入れない）
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
    msg = generate_deep_text()
    if msg:
        try:
            client_x.create_tweet(text=msg)
            print(f"✅ 成功:\n{msg}")
        except Exception as e:
            print(f"❌ X投稿エラー: {e}")

if __name__ == "__main__":
    post()
