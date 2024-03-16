# pythonのイメージをダウンロード
FROM python:3.11.3

# 作業ディレクトリを指定
WORKDIR /app

# ホストマシンのrequirements.txtをコンテナにコピー
COPY requirements.txt .

# 依存ライブラリをインストール
RUN pip install -r requirements.txt

# ホストマシンのファイルをコンテナにコピー
COPY . .

# コンテナのデフォルトの実行コマンド
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
