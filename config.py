from dataclasses import dataclass
from crawl4ai import CrawlerRunConfig

# RSSフィードのURL
RSS_URL = "RSS_URL"

# DiscordのWebhook URL
DISCORD_WEBHOOK_URL = "DISCORD_WEBHOOK_URL"

# 使用するOllamaモデルの名前
OLLAMA_MODEL_NAME = 'figure-extractor'

# 最後に取得したRSSアイテムの情報を保存するファイル
TIMESTAMP_FILE = 'last_item.json'

# Webクローラーの設定
CRAWLER_CONFIG = CrawlerRunConfig(
    exclude_external_images=True,  # 外部画像を除外
)

# Ollamaに渡すプロンプトの最大文字数
MAX_PROMPT_LENGTH = 4096


@dataclass
class SummaryInfo:
    """要約情報を格納するデータクラス。"""
    name: str
    doc: str
    price: str
    url: str


def discord_payload(summary_info, url) -> dict:
    return {
        "content": f"[情報元URL]({url})",
        "embeds": [
            {
                "title": summary_info.name,
                "description": summary_info.doc,
                "fields": [
                    {"name": "価格", "value": summary_info.price, "inline": False},
                    {"name": "関連するURL", "value": summary_info.url, "inline": False}
                ],
                "url": summary_info.url
            }
        ]
    }
