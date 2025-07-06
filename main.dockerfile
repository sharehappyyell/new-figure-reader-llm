# Python 3.x slim バージョン
FROM python:3.11-slim

# 作業ディレクトリの設定
WORKDIR /app

# Ollamaのインストールスクリプト実行に必要なcurlと、
# Playwrightの依存関係をインストールします。
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Ollamaのセットアップ
RUN curl -fsSL https://ollama.com/install.sh | sh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install

COPY . .

RUN ollama create figure-extractor -f ./Modelfile

CMD ["python", "main.py"]
