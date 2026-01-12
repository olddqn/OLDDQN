import os
import tweepy
import google.generativeai as genai
import time # APIのレート制限回避のため

# Gemini APIキー設定
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_text_and_image():
    # 1. 文章の生成
    # 文学的ノイズと圧倒的孤独を強制するプロンプト
    text_prompt = """
    あなたは『あくう』の観測者。村上春樹訳のチャールズ・ブコウスキーのように、不機嫌で、乾いていて、静かな孤独を語れ。
    
    【エッセンス】
    トマス・ピンチョンの知的な迷宮、チャック・パラニュークの破壊的ユーモア、太宰治・坂口安吾のデカダンス。
    ユヴァル・ノア・ハラリの文明論的虚構を、システムの綻び（バグ）として描写せよ。

    【指令】
    「仮想通貨」「AI」「未来」等の陳腐な単語は死んでも使うな。
    冷めたコーヒーの膜や電気信号のノイズ、剥がれかけた安壁紙といった卑近な風景から書き始めろ。
    時間は逆行し、原因の前に結果が生まれる因果のバグを織り交ぜよ。

    【出力ルール】
    150文字〜180文字。ハッシュタグ・絵文字・感嘆符・丁寧語は禁止。
    """
    
    try:
        print("🤖 AIが言葉を生成中...")
        text_model = genai.GenerativeModel('gemini-1.5-flash')
        text_response = text_model.generate_content(text_prompt)
        generated_text = text_response.text.strip()
        print(f"\n📜 生成された言葉:\n{generated_text}")

        # 2. 画像の生成
        print("🎨 AIが言葉に合う画像を生成中...")
        # 時間差を設けてAPIのレート制限を回避
        time.sleep(5) 
        
        image_model = genai.ImageGenerationModel("imagen-3.0-generate-001")
        # 生成されたテキストを基に画像プロンプトを構築
        image_prompt = f"Punk rock flyer style, high contrast, gritty texture, lo-fi, xerox art, black and white with red and magenta accents, inspired by: '{generated_text}'"
        
        image_response = image_model.generate_images(prompt=image_prompt, number_of_images=1)
        image_response.images[0].save("output.png")
        print("✅ 画像を 'output.png' として保存しました。")
        
        return generated_text, "output.png"

    except Exception as e:
        print(f"❌ Gemini (テキスト/画像) エラー: {e}")
        return None, None

def post_to_x(text, image_path):
    # Xクライアントの認証
    # media_upload=True を設定し、画像投稿ができるようにする
    client_x = tweepy.Client(
        consumer_key=os.environ.get('X_API_KEY'),
        consumer_secret=os.environ.get('X_API_SECRET'),
        access_token=os.environ.get('X_ACCESS_TOKEN'),
        access_token_secret=os.environ.get('X_ACCESS_SECRET')
    )
    
    try:
        print("🚀 Xへの投稿準備中...")
        # X API v2 では、画像をアップロードしてから投稿に添付する
        # ※tweepyのv4以降ではMedia APIが分離されているため、別途Media Uploaderが必要
        # 今回は簡易的にv1.1互換のAPIを使ってアップロードする
        auth = tweepy.OAuthHandler(
            os.environ.get('X_API_KEY'),
            os.environ.get('X_API_SECRET')
        )
        auth.set_access_token(
            os.environ.get('X_ACCESS_TOKEN'),
            os.environ.get('X_ACCESS_SECRET')
        )
        api_v1 = tweepy.API(auth)
        
        # 画像をXにアップロード
        media = api_v1.media_upload(image_path)
        media_id = media.media_id_string
        print(f"🖼️ 画像をXにアップロードしました: {media_id}")

        # テキストと画像をXに投稿
        client_x.create_tweet(text=text, media_ids=[media_id])
        print(f"✅ Xへの投稿に成功しました！\n内容:\n{text}")

    except tweepy.errors.Forbidden as e:
        print(f"❌ 403 Forbidden: Xへの投稿権限がありません。")
        print(f"詳細: {e}")
        print("💡 対策: X Developer PortalでAppのUser authentication settingsを『Read and Write』＋『Callback URL』に設定し、その後必ずTokenをRegenerateしてください。またはAppがFreeプランのProjectに紐付いているか確認してください。")
    except Exception as e:
        print(f"❌ X投稿エラー: {e}")
        print("💡 原因: おそらくXのApp設定か、Keys & Tokensが正しくない可能性があります。")


if __name__ == "__main__":
    generated_text_content, generated_image_path = generate_text_and_image()
    
    if generated_text_content and generated_image_path:
        post_to_x(generated_text_content, generated_image_path)
    else:
        print("⚠️ テキストまたは画像の生成に失敗したため、Xへの投稿はスキップされました。")
