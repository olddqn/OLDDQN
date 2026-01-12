import os
import tweepy

def main():
    print("🛠️ --- X(Twitter) 権限診断テスト開始 ---")
    
    # 1. 鍵の読み込みチェック
    keys = {
        "Consumer Key": os.environ.get('X_API_KEY'),
        "Consumer Secret": os.environ.get('X_API_SECRET'),
        "Access Token": os.environ.get('X_ACCESS_TOKEN'),
        "Access Token Secret": os.environ.get('X_ACCESS_SECRET')
    }

    for name, value in keys.items():
        if not value:
            print(f"❌ エラー: {name} が設定されていません。GitHub Secretsを確認してください。")
            return
        print(f"✅ {name}: 読み込み完了 (末尾: ...{value[-4:]})")

    try:
        # 2. クライアント初期化
        client = tweepy.Client(
            consumer_key=keys["Consumer Key"],
            consumer_secret=keys["Consumer Secret"],
            access_token=keys["Access Token"],
            access_token_secret=keys["Access Token Secret"]
        )

        # 3. テスト投稿試行
        test_msg = "システムテスト: 観測。接続確認。"
        print(f"\n📡 投稿を試行中: {test_msg}")
        
        response = client.create_tweet(text=test_msg)
        print("\n✨【大成功】Xに投稿されました！権限設定は完璧です。")
        print(f"Tweet ID: {response.data['id']}")

    except tweepy.TweepyException as e:
        print(f"\n❌ 投稿失敗: {e}")
        print("-" * 30)
        error_str = str(e)
        
        if "403" in error_str:
            print("【診断結果: 403 Forbidden】")
            print("原因: 鍵は合っていますが『書き込み許可』がありません。")
            print("解決策:")
            print("1. X Developer Portalで App permissions を 'Read and Write' に変更。")
            print("2. 変更後に必ず 'Save' ボタンを押す。")
            print("3. その後、Access Token と Secret を必ず『Regenerate(再発行)』してください。")
            print("   ※古い鍵には書き込み権限が乗っていません。")
        elif "401" in error_str:
            print("【診断結果: 401 Unauthorized】")
            print("原因: 鍵そのものが間違っているか、コピペミス（スペース混入等）です。")
            print("解決策: 全ての鍵を再発行し、GitHub Secretsに慎重に貼り直してください。")
        print("-" * 30)

if __name__ == "__main__":
    main()
