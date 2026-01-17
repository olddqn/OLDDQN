import os
import time
import tweepy
from google import genai

# --- 1. Geminiでテキストを生成する関数 ---
def generate_akuh_text():
    try:
        # 有料版でも404を出さないための最もシンプルな接続方法
        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        
        prompt = """
        あなたは観測者「あくう」。
        遠藤ミチロウ、ビートたけし、村上春樹、太宰治を混ぜ合わせた虚無の存在。
        「成功」や「秩序」を冷笑する独白を日本語135文字以内で。
        丁寧語禁止、ハッシュタグ不要。
        """
        
        # 404を回避するため 'models/' を含めない
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text.strip()[:135]
    except Exception as e:
        print(f"Geminiエラー: {e}")
        return None

# --- 2. Xに投稿する関数 ---
def post_to_x(text):
    if not text: return
    try:
        client = tweepy.Client(
            consumer_key=os.environ["X_API_KEY"],
            consumer_secret=os.environ["X_API_SECRET"],
            access_token=os.environ["X_ACCESS_TOKEN"],
            access_token_secret=os.environ["X_ACCESS_SECRET"],
        )
        client.create_tweet(text=text)
        print(f"投稿成功: {text[:20]}...")
    except Exception as e:
        print(f"X投稿エラー: {e}")

# --- 3. メイン実行部分 ---
if __name__ == "__main__":
    print("📡 侵食開始...")
    text = generate_akuh_text()
    if text:
        post_to_x(text)
    else:
        print("❌ テキストが生成されなかったため投稿を中止しました")
