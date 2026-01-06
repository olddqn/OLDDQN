import os
import tweepy
from google import genai

# Gemini初期化
def generate_text():
    try:
        client_gemini = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
        prompt = "あなたは孤独な観測者。村上春樹訳のブコウスキー風に、今の世界のノイズについて140文字以内で短く吐き捨てて。丁寧語禁止。"
        response = client_gemini.models.generate_content(model="gemini-1.5-flash", contents=prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Geminiエラー: {e}")
        return None

def main():
    msg = generate_text()
    if not msg: return

    # X 認証
    try:
        client_x = tweepy.Client(
            consumer_key=os.environ.get('X_API_KEY'),
            consumer_secret=os.environ.get('X_API_SECRET'),
            access_token=os.environ.get('X_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('X_ACCESS_SECRET')
        )
        
        # 投稿実行
        client_x.create_tweet(text=msg)
        print(f"✅ 成功！投稿内容:\n{msg}")

    except tweepy.errors.Forbidden as e:
        print(f"❌ 403 Forbidden: まだ権限がありません。")
        print(f"理由: {e}")
        print("💡 対策: AppのUser authentication settingsで『Read and Write』＋『Callback URL』を設定後、必ずTokenをRegenerateしてください。")
    except Exception as e:
        print(f"❌ 予期せぬエラー: {e}")

if __name__ == "__main__":
    main()
