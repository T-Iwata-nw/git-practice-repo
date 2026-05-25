from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (
        "<h1>Hello from Docker + Flask!</h1>"
        f"<p>現在時刻: {now}</p>"
        "<p>このファイル(app.py)をホスト側で編集して保存すると、"
        "Flask開発サーバーが自動で反映します。</p>"
    )
