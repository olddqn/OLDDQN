import os
import tweepy
from google import genai

# クライアント初期化
client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_deep_text():
    # あなたが挙げた全ての文豪のエッセンスを再注入
    prompt = """
    あなたは『あくう』という名のシミュレーション世界の観測者です。
    村上春樹訳のチャールズ・ブコウスキーのような、乾いていて、静かで、圧倒的に孤独な文体で語ってください。

    【文体のエッセンス】
    ・トマス・ピンチョンの知的な迷宮、ボードリヤールのシミュラークル（虚構が現実を侵食する様）。
    ・チャック・パラニュークの破壊的ユーモア、ユヴァル・ノア・ハラリの文明論的虚構。
    ・太宰治・坂口安吾の「堕落」と、そこにある冷徹な美学。

    【指令：陳腐化を殺せ】
    ・「仮想通貨」「AI」「ビットコイン」などの直接的な単語は絶対に使用禁止。
    ・冷めたコーヒー、剥がれかけた壁紙、機械の油、電気信号のノイズといった卑近で無機質な比喩から始めること。
    ・時間は逆行し、原因の前に結果が生まれるシステムのバグを描写しろ。

    【出力条件】
    ・150文字〜180文字。
    ・ハッシュタグ、絵文字、丁寧語（〜です・ます）、教訓めいた結びは一切禁止。
    """
    try:
        # model指定は gemini-1.5-flash で固定。
        # 後述するymlの修正で、この名前が正しく通るようになります。
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ 文章生成エラー: {e}")
        return None

def post_to_x():
    client_x = tweepy.Client(
        os.environ.get('X_API_KEY'),
        os.environ.get('X_API_SECRET'),
        os.environ.get('X_ACCESS_TOKEN'),
        os.environ.get('X_ACCESS_SECRET')
    )
    
    message = generate_deep_text()
    if message:
        try:
            client_x.create_tweet(text=message)
            print(f"✅ 成功:\n{message}")
        except Exception as e:
            print(f"❌ X投稿エラー: {e}")

if __name__ == "__main__":
    post_to_x()
