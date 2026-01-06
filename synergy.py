import os
import tweepy
from google import genai

# --- 1. クライアント初期化 ---
# Gemini (AI)
client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

# X (Twitter) - 4つの鍵を環境変数から取得
def get_x_client():
    return tweepy.Client(
        consumer_key=os.environ.get('X_API_KEY'),
        consumer_secret=os.environ.get('X_API_SECRET'),
        access_token=os.environ.get('X_ACCESS_TOKEN'),
        access_token_secret=os.environ.get('X_ACCESS_SECRET')
    )

# --- 2. 文生成関数 ---
def generate_text():
    prompt = """
    あなたは『あくう』の観測者。村上春樹訳のブコウスキーのように、不機嫌で、静かで、圧倒的に孤独な文体で語れ。
    150文字程度。ハッシュタグ・絵文字・丁寧語禁止。
    テーマ：時間の逆行、冷めたコーヒー、電気信号のノイズ。
    """
    try:
        response = client_gemini.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini文章生成エラー: {e}")
        return None

# --- 3. メイン処理 ---
def main():
    # 文言作成
    msg = generate_text()
    if not msg:
        return

    # Xへの投稿
    try:
        client_x = get_x_client()
        client_x.create_tweet(text=msg)
        print(f"✅ ついに成功！Xに投稿されました:\n{msg}")
    except Exception as e:
        print(f"❌ X投稿失敗: {e}")
        print("💡 これで失敗する場合、トークンの『再発行(Regenerate)』と『GitHub上書き』を今一度確認してください。")

if __name__ == "__main__":
    main()
