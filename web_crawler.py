from crawl4ai import AsyncWebCrawler
from typing import Optional

# 設定ファイルからクローラー設定をインポート
from config import CRAWLER_CONFIG


async def get_content_from_url(url: str) -> Optional[str]:
    """
    指定されたURLからコンテンツをクロールし、Markdown形式で返す。
    """
    print(f"🔄 URLからコンテンツを取得しています: {url}")
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=url, config=CRAWLER_CONFIG)
            content = result.markdown

            if not content:
                print("❌ コンテンツの取得に失敗しました。")
                return None

            print("✅ コンテンツの取得完了。")
            return content

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None
