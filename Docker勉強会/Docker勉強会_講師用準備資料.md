# Docker 勉強会 講師用準備資料

**日時：** 2026年（調整中）  
**所要時間：** 80分  
**対象：** 情報システム部員（Git勉強会参加者・Docker初心者）  

---

## 目次

1. [勉強会の全体設計](#1-勉強会の全体設計)
2. [事前準備チェックリスト（講師）](#2-事前準備チェックリスト講師)
3. [タイムライン詳細](#3-タイムライン詳細)
4. [ハンズオン環境の準備](#4-ハンズオン環境の準備)
5. [トラブルシューティング](#5-トラブルシューティング)

---

## 1. 勉強会の全体設計

### タイムライン概要

| 時間 | パート | 内容 | 形式 |
|------|--------|------|------|
| 0:00〜0:05 | 開始・接続確認 | Docker Desktopの起動確認 | 全員確認 |
| 0:05〜0:15 | Linuxコマンドの基本 | 必要なコマンドを絞って説明 | 講師説明 |
| 0:15〜0:30 | Dockerの基本・Docker Hub | 概念・アーキテクチャの説明 | 講師説明 |
| 0:30〜0:40 | Dockerコマンド・hello-world | コマンド解説＋全員で実行 | 実演＋全員操作 |
| 0:40〜0:50 | Dockerfile・docker-compose | ファイルの書き方を解説 | 講師説明 |
| 0:50〜1:05 | ハンズオン① | JupyterLab環境を構築 | 全員操作 |
| 1:05〜1:15 | Dev Container | 概念説明・拡張機能インストール・デモ | 講師説明＋実演 |
| 1:15〜1:18 | まとめ・質疑 | 振り返りとQ&A | 全員 |

### 受講者の前提知識

- Git勉強会参加済み（コマンドライン操作・ファイル操作の基本あり）
- ターミナル（コマンドプロンプト）操作の経験あり
- Docker・Linuxは未経験

---

## 2. 事前準備チェックリスト（講師）

### 勉強会1週間前まで

- [ ] ハンズオン用の `docker-compose.yml` を作成・動作確認済み
- [ ] `docker-compose.yml` と `.env`（必要な場合）を受講者に事前配布
- [ ] 受講者事前準備資料を配布し、Docker Desktopのインストールを依頼済み
- [ ] 講師PCでハンズオン手順を最初から最後まで通しで動作確認済み
- [ ] Dev Container デモ用プロジェクトを作成・動作確認済み（後述）
- [ ] VS CodeにDev Containers拡張機能をインストール済み

### 勉強会前日まで

- [ ] Docker Desktopが起動できる（クジラアイコンが表示される）
- [ ] `docker run hello-world` が正常に動作する
- [ ] ハンズオン用フォルダ構成が準備できている（下記参照）
- [ ] プロジェクター・画面共有の準備が整っている
- [ ] ターミナルのフォントサイズを大きくした（受講者が見やすいよう）

### 当日

- [ ] Docker Desktop が起動している（タスクトレイのクジラアイコンを確認）
- [ ] 受講者全員のDocker Desktopが起動できていることを確認
- [ ] ハンズオン用ファイルの配布方法を確認（チャット・共有フォルダ等）

---

## 3. タイムライン詳細

### 0:00〜0:05 開始・接続確認

**講師セリフ例：**
> 「まず全員のDocker Desktopが起動しているか確認してください。タスクトレイ（画面右下）にクジラのアイコンが表示されていればOKです。」

確認事項：
- タスクトレイにクジラアイコンがある
- アイコンが「Docker Desktop is running」になっている（赤や黄色でないこと）

---

### 0:05〜0:15 Linuxコマンドの基本

**講師セリフ例：**
> 「DockerはLinux上で動いているため、基本的なLinuxコマンドを知っておく必要があります。Gitのときに使ったGit Bashと同じ感覚で使えます。」

実演コマンド（PowerShellまたはターミナルで）：

```bash
pwd          # 現在のフォルダを表示
ls           # フォルダの中身を一覧表示
ls -la       # 隠しファイルも含めて詳細表示
mkdir test   # フォルダを作成
cd test      # フォルダに移動
cd ..        # 1つ上のフォルダに移動
cat ファイル名  # ファイルの内容を表示
```

**ポイント：**
- Git BashでもPowerShellでも同じコマンドが使えることを伝える
- `ls` と `dir` の違い（Windowsの場合）には触れすぎない

---

### 0:15〜0:30 Dockerの基本・Docker Hub

**Dockerとは：**
> 「アプリケーションとその動作環境をまるごとパッケージにして、どこでも同じ環境を再現できる仕組みです。」

**説明すべき概念（図を使って説明）：**

- イメージ vs コンテナの違い
- ホストOS・Docker Engine・コンテナの関係
- Docker Hub（イメージの配布場所）

**Gitとの対比でGitHub比較（受講者が理解しやすい）：**

| Git/GitHub | Docker/Docker Hub |
|-----------|------------------|
| コード（ファイル） | イメージ |
| git commit | docker build |
| GitHub | Docker Hub |
| git pull | docker pull |
| git push | docker push |

---

### 0:30〜0:40 Dockerコマンド・hello-world

**全員で実行するコマンド：**

```bash
# hello-worldイメージを取得して実行（初めてのdockerコマンド）
docker run hello-world

# 取得済みイメージの一覧
docker images

# 実行中のコンテナ一覧
docker ps

# 終了済みも含めたコンテナ一覧
docker ps -a
```

**hello-world実行時の出力解説：**
> 「`Unable to find image 'hello-world:latest' locally` → ローカルにないのでDocker Hubから自動でpullしています。`Hello from Docker!` と表示されればコンテナが正常に実行されました。」

**`docker ps -a` で状態を見せる：**
> 「hello-worldコンテナはメッセージを表示して即終了します。`docker ps -a` でStatusが`Exited (0)`になっていることを確認してください。」

#### hello-worldではbashに入れない理由を説明する

> 「hello-worldは最小限のイメージで、bashが入っていません。`docker exec -it hello-world bash` と打ってもエラーになります。コンテナ内を操作するには、bashが含まれるイメージが必要です。」

**よくある間違いを先に見せる（受講者が同じ失敗をしないように）：**

```bash
# ❌ これはエラーになる（コンテナIDを指定しているが停止中のため）
docker exec -it ac0cb108d20b bash
# → Error response from daemon: container ... is not running

# ❌ これもエラー（コンテナ名ではなくイメージ名を指定しているため）
docker exec -it hello-world bash
# → Error response from daemon: No such container: hello-world
```

#### ubuntuコンテナでbash実践

```bash
# ubuntuイメージでコンテナを起動してbashに入る
docker run -it ubuntu bash
# → プロンプトが root@コンテナID:/# に変わる

# コンテナ内で打つコマンド
pwd           # → /
ls            # → Linuxのフォルダ一覧が表示される
cd /home
mkdir test-folder
echo "Hello from container!" > hello.txt
cat hello.txt
cat /etc/os-release   # → Ubuntuであることがわかる

# コンテナから出る
exit

# 出た後に確認
docker ps -a   # → Exited になっている
docker images  # → ubuntu:latest は残っている
```

**「コンテナは使い捨て」を実感させるポイント：**
> 「コンテナ内で作ったファイルや、apt installしたものは、コンテナを削除すると消えます。次回 `docker run` すると真っさらな状態から始まります。これが『コンテナは使い捨て可能』という意味です。」

---

### 0:40〜0:50 Dockerfile・docker-compose

**Dockerfile説明ポイント：**
- イメージを「作る」ためのレシピ
- `FROM`・`RUN`・`COPY`・`CMD` の4つを中心に説明

**docker-compose説明ポイント：**
- 複数のコンテナをまとめて管理するツール
- YAMLファイルで設定を記述する
- `docker-compose up` 1コマンドで環境が立ち上がる

---

### 0:50〜1:15 ハンズオン

詳細は [セクション4](#4-ハンズオン環境の準備) 参照。

**講師の進行イメージ：**
1. `docker-compose.yml` の内容を画面で共有しながら説明（5分）
2. 受講者が各自ターミナルでコマンドを実行
3. ブラウザで `http://localhost:8888` にアクセスして確認
4. JupyterLabが開いたら、Notebookを1つ作成してPythonが動くことを確認

---

### 1:05〜1:15 Dev Container

> **このパートは講師デモ中心です。受講者は画面を見ながら概念を理解します。**  
> 時間の余裕があれば受講者にも拡張機能のインストールと起動まで体験してもらいます。

**講師セリフ例：**
> 「ここまでdocker-composeでJupyterLab環境を作りました。次はVS Codeから直接Dockerコンテナの中で開発する『Dev Container』という仕組みを紹介します。Git勉強会でVS CodeのGit機能を使いましたが、Dev ContainerはVS Codeをそのままコンテナの中に持ち込むイメージです。」

**説明ポイント：**
1. Dev Containerとdocker-composeの違い（JupyterLab vs VSCode内での開発）
2. `.devcontainer/devcontainer.json` の役割
3. 起動デモ（後述のデモ用プロジェクトを使用）
4. 左下の表示が変わること（`><` → `Dev Container: ...`）を見せる
5. コンテナ内ターミナルで `python --version` を実行して環境が切り替わっていることを確認

**デモのゴール：**
VS Codeがコンテナに接続した状態を見せ、「ローカルにPythonをインストールしなくてもコンテナ内のPythonを使って開発できる」ことを体感させる。

---

### 1:15〜1:18 まとめ・質疑

振り返りのポイント：
- コンテナはPC内の「使い捨て可能な実行環境」
- docker-composeで環境定義をコード化できる（Gitで管理可能）
- Dev Containerを使うとVS Codeのままコンテナ内で開発できる
- 今後の活用：開発環境の標準化、ベンダーへの環境仕様共有、チーム全員が同じ環境で開発

---

## 4. ハンズオン環境の準備

### ハンズオンの目的

`docker-compose.yml` を使って、Anaconda + JupyterLab の Python 環境をコンテナ上に構築する。ローカルのフォルダをマウントして、作成したNotebookがPC上に保存されることを確認する。

### 必要なフォルダ構成

受講者のPCで以下のフォルダ構成を作成してもらいます：

```
docker-jupyter/                   ← プロジェクトフォルダ
├── docker-compose.yml            ← 講師が事前に作成して配布
└── notebooks/                    ← マウント先フォルダ（空でOK）
```

### 配布ファイル：`docker-compose.yml`

```yaml
version: '3.8'

services:
  jupyter:
    image: continuumio/anaconda3
    container_name: jupyter-lab
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/notebooks
    working_dir: /notebooks
    command: >
      /bin/bash -c "
      pip install jupyterlab &&
      jupyter lab
      --ip=0.0.0.0
      --port=8888
      --no-browser
      --allow-root
      --NotebookApp.token=''
      --NotebookApp.password=''
      "
    restart: unless-stopped
```

### ハンズオン実行コマンド

```bash
# 1. プロジェクトフォルダに移動
cd docker-jupyter

# 2. コンテナを起動（初回はイメージのダウンロードがあるため数分かかる）
docker-compose up

# 3. ブラウザで http://localhost:8888 を開く
#    JupyterLabが表示されればOK

# 4. 終了するときは Ctrl + C を押してから
docker-compose down
```

### 初回起動時の注意

- Anacondaイメージは約3GBあるため、**ダウンロードに時間がかかります**（環境により5〜15分）
- **勉強会前日までにイメージのダウンロードを完了しておくよう受講者に依頼する**
- 受講者事前準備資料にダウンロード手順を記載済み

### 動作確認手順（講師）

```bash
# 事前に通しで確認する
mkdir docker-jupyter
cd docker-jupyter
mkdir notebooks
# docker-compose.yml を上記内容で作成
docker-compose up
# → ブラウザで http://localhost:8888 を開く
# → JupyterLabが表示されることを確認
# → Notebookを作成してPythonコードが動くことを確認（例：print("Hello")）
# → notebooks/ フォルダにファイルが保存されることを確認
docker-compose down
```

---

## 5. Dev Containerデモ環境の準備

### デモ用プロジェクトのフォルダ構成

```
devcontainer-demo/
├── .devcontainer/
│   └── devcontainer.json
└── hello.py
```

### `.devcontainer/devcontainer.json`（デモ用）

```json
{
  "name": "Python Dev Container Demo",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  },
  "postCreateCommand": "pip install requests pandas"
}
```

### `hello.py`（デモ用）

```python
import sys
import pandas as pd

print("Hello from Dev Container!")
print(f"Python: {sys.version}")
print(f"pandas: {pd.__version__}")
```

### デモ手順（講師画面共有）

```bash
# 1. デモ用プロジェクトフォルダを作成
mkdir devcontainer-demo
cd devcontainer-demo
mkdir .devcontainer

# 2. 上記の2ファイルを作成（テキストエディタまたはVS Codeで）

# 3. VS Codeでフォルダを開く
code .

# 4. VS Codeで左下「><」→「コンテナで再度開く」をクリック
#    → 初回はイメージのpullが発生（数分）

# 5. 左下に「Dev Container: Python Dev Container Demo」と表示されたら起動完了

# 6. VS Codeのターミナルで実行
python hello.py
# → "Hello from Dev Container!" が表示されることを確認

# 7. ローカルターミナルで python --version を実行して「コンテナ内のPythonと違う」ことを見せる
```

> **デモのポイント：** 手順6でコンテナ内のPythonが動いていること、手順7でローカルとバージョンが異なることを比較して見せると、「環境が分離されている」ことが直感的に伝わります。

### 事前に確認しておくこと

- [ ] `mcr.microsoft.com/devcontainers/python:3.11` イメージを事前にpull済み
- [ ] デモ用フォルダで `Reopen in Container` が正常に動作することを確認済み
- [ ] `hello.py` が正常に実行できることを確認済み

```bash
# 事前にイメージをpullしておく
docker pull mcr.microsoft.com/devcontainers/python:3.11
```

---

## 6. トラブルシューティング

### Docker Desktopが起動しない

**症状：** タスクトレイにクジラアイコンが表示されない、またはエラーになる  
**対処：**
1. PCを再起動してDocker Desktopを起動し直す
2. BIOSの仮想化（Virtualization）が有効になっているか確認
3. WSL2のインストール状況を確認（Windowsの場合）

```powershell
# WSL2の確認（PowerShellで実行）
wsl --status
```

### `docker run hello-world` でエラーになる

**症状：** `Cannot connect to the Docker daemon` と表示される  
**対処：** Docker Desktopが起動していない。タスクトレイのクジラアイコンを確認し、起動を待つ

### `docker-compose up` でポートエラーになる

**症状：** `Bind for 0.0.0.0:8888 failed: port is already allocated`  
**対処：** 8888ポートが他のアプリに使われている

```bash
# 別のポートに変更する（docker-compose.ymlを編集）
ports:
  - "8889:8888"   # ← 左側の数字を変更
# → ブラウザで http://localhost:8889 を開く
```

### JupyterLabのURLが表示されない・ブラウザで開けない

**症状：** ターミナルにURLが表示されるがブラウザで開けない  
**対処：**
1. `http://localhost:8888` を直接ブラウザのアドレスバーに入力
2. `http://127.0.0.1:8888` でも試す
3. ファイアウォールが8888番ポートをブロックしていないか確認

### イメージのダウンロードが遅い・タイムアウトする

**対処：**
- Wi-Fiに切り替えるか、有線LANを使用する
- 社内プロキシの設定が必要な場合は IT管理者に確認する

### `notebooks/` フォルダにファイルが保存されない

**対処：**
- `docker-compose.yml` の `volumes` のパスが正しいか確認
- `./notebooks` はdocker-compose.ymlと**同じフォルダ内**の `notebooks` フォルダを指している

```bash
# フォルダ構成を確認
ls -la
# → docker-compose.yml と notebooks/ が同じフォルダにあることを確認
```

### Dev Container が起動しない（「コンテナで再度開く」が出ない）

**症状：** VS Codeを開いても `Reopen in Container` の通知が出ない  
**対処：**
1. `.devcontainer/devcontainer.json` がプロジェクトフォルダのルートに存在するか確認
2. VS Codeに「Dev Containers」拡張機能がインストールされているか確認
3. 左下の `><` アイコンをクリック →「コンテナーで再度開く」を手動で選択

### Dev Container 起動時に「Docker daemon is not running」エラー

**対処：** Docker Desktopが起動していない。タスクトレイのクジラアイコンを確認して起動を待つ

### Dev Container 内で拡張機能が表示されない

**症状：** ローカルでインストールした拡張機能がコンテナ内で使えない  
**原因：** Dev Container内のVS Codeはコンテナ側に別途拡張機能をインストールする必要がある  
**対処：** `devcontainer.json` の `customizations.vscode.extensions` に必要な拡張機能のIDを追記してコンテナを再ビルドする

---

## 参考：当日共有するコマンドまとめ

受講者にチャット等で共有するコマンド一覧：

```bash
# ===== Linuxコマンド基本 =====
pwd                        # 現在のフォルダを表示
ls                         # フォルダの内容を表示
mkdir フォルダ名             # フォルダを作成
cd フォルダ名               # フォルダに移動
cd ..                      # 1つ上のフォルダに移動
cat ファイル名               # ファイルの内容を表示

# ===== Dockerコマンド基本 =====
docker --version           # Dockerのバージョン確認
docker run hello-world     # hello-worldコンテナを実行
docker images              # ローカルのイメージ一覧
docker ps                  # 実行中のコンテナ一覧
docker ps -a               # 全コンテナ一覧（停止中含む）
docker pull イメージ名       # イメージを取得
docker stop コンテナ名       # コンテナを停止
docker rm コンテナ名         # コンテナを削除
docker rmi イメージ名        # イメージを削除

# ===== ハンズオン =====
cd docker-jupyter          # フォルダに移動
docker-compose up          # コンテナを起動
docker-compose down        # コンテナを停止・削除
docker-compose up -d       # バックグラウンドで起動
docker-compose logs        # ログを確認
```

---

*作成日：2026年*  
*対象：情報システム部 Docker勉強会 講師*
