from crawl4ai import AsyncWebCrawler
from typing import Optional

# 設定ファイルからクローラー設定をインポート
from config import CRAWLER_CONFIG, BROWSER_CONFIG


async def get_content_from_url(url: str) -> Optional[str]:
    """
    指定されたURLからコンテンツをクロールし、コンテンツを返す。
    """
    async with AsyncWebCrawler(config=BROWSER_CONFIG) as crawler:
        return await crawler.arun(url=url, config=CRAWLER_CONFIG)
