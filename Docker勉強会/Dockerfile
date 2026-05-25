# ベースイメージを指定（python:3.11-slim はフルイメージより約800MB軽い）
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なライブラリをインストール
# JupyterLab（数百MB）の代わりに、軽量Webフレームワークの Flask（数MB）を使う
RUN pip install --no-cache-dir flask

# Flask開発サーバーの設定
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1

# Flaskが使用するポートを公開
EXPOSE 5000

# コンテナ起動時に Flask 開発サーバーを起動
# --host=0.0.0.0 を指定することで、ホストPCのブラウザからアクセス可能になる
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
