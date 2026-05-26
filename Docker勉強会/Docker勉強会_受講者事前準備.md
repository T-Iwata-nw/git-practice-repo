# Docker 勉強会 受講者事前準備手順書

**勉強会日時：** 2026年（調整中）  
**所要時間（準備）：** 約30〜45分（ダウンロード時間を含む）  

> **勉強会当日までに、この手順書の準備を完了させてください。**  
> 特にDockerイメージのダウンロード（約3GB）は時間がかかるため、**前日までに必ず完了**させてください。  
> 不明な点は事前に講師に確認をお願いします。

---

## 準備の全体像

```
STEP 1: Docker Desktop のインストール
    ↓
STEP 2: Docker Desktop の起動確認
    ↓
STEP 3: 動作確認（hello-world）
    ↓
STEP 4: ハンズオン用イメージの事前ダウンロード（重要）
    ↓
STEP 5: VS Code 拡張機能「Dev Containers」のインストール
    ↓
STEP 6: ハンズオン用リポジトリの取得（git pull）
```

---

## STEP 1: Docker Desktop のインストール

### インストール済みか確認する

1. スタートメニューで「Docker Desktop」を検索する
2. 「Docker Desktop」が見つかればインストール済みです → **STEP 2 に進む**
3. 見つからない場合は以下の手順でインストールします

### システム要件の確認

| 項目 | 要件 |
|------|------|
| OS | Windows 10 64bit（バージョン1903以降）/ Windows 11 |
| CPU | 仮想化（Virtualization）が有効になっていること |
| メモリ | 4GB以上（8GB推奨） |
| ディスク空き容量 | 10GB以上 |

### インストール手順

1. ブラウザで **`https://www.docker.com/products/docker-desktop/`** を開く

2. 「Download for Windows」をクリックしてインストーラーをダウンロード  
   （ファイル名例：`Docker Desktop Installer.exe`）

3. ダウンロードしたインストーラーをダブルクリックして実行

4. 「ユーザーアカウント制御」のダイアログが出たら「はい」をクリック

5. インストール設定画面が表示されます。以下の設定にチェックが入っていることを確認して「OK」：
   - [x] **Use WSL 2 instead of Hyper-V（recommended）**  ← チェックを入れる
   - [x] Add shortcut to desktop

6. インストールが完了したら「Close and restart」をクリックしてPCを再起動

> **WSL2とは：** Windows上でLinuxを動かす仕組みです。Docker DesktopはWSL2を利用して動作します。

---

## STEP 2: Docker Desktop の起動確認

### Docker Desktop を起動する

1. スタートメニューまたはデスクトップのショートカットから「Docker Desktop」を起動

2. 初回起動時はセットアップが走ります（数分かかる場合があります）

3. 画面右下のタスクトレイ（通知領域）にクジラのアイコンが表示されることを確認

```
タスクトレイの状態：
🐳  → Docker Desktop is running（緑 / 通常状態）← これがOKな状態
⏳  → Docker Desktop is starting（起動中）
⚠️  → エラーあり（後述のトラブルシューティング参照）
```

4. クジラアイコンを右クリックして「Dashboard」を開き、緑のランプと「Engine running」が表示されていることを確認

---

## STEP 3: 動作確認（hello-world）

### ターミナルを開く

以下のいずれかの方法でターミナルを開きます：

- **PowerShell：** スタートメニューで「PowerShell」を検索して起動
- **コマンドプロンプト：** スタートメニューで「cmd」を検索して起動
- **Git Bash：** デスクトップで右クリック →「Git Bash Here」（Git勉強会でインストール済み）

### Dockerのバージョンを確認する

```bash
docker --version
```

以下のように表示されればOKです：

```
Docker version 27.x.x, build xxxxxxx
```

（バージョン番号は異なっていても問題ありません）

### hello-worldコンテナを実行する

```bash
docker run hello-world
```

以下のような出力が表示されればインストール成功です：

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
...
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

---

## STEP 4: ハンズオン用イメージの事前ダウンロード（重要）

ハンズオンで使用するAnacondaイメージは**約3GB**あります。勉強会当日にダウンロードすると時間がかかってしまうため、**必ず前日までにダウンロードを完了させてください。**

### イメージをダウンロードする

ターミナルで以下のコマンドを実行します：

```bash
docker pull continuumio/anaconda3
```

ダウンロード中は以下のような表示が続きます（環境によって5〜20分かかります）：

```
latest: Pulling from continuumio/anaconda3
xxxxxxxx: Pulling fs layer
xxxxxxxx: Pulling fs layer
...
xxxxxxxx: Pull complete
...
Status: Downloaded newer image for continuumio/anaconda3:latest
```

最後に `Status: Downloaded newer image for continuumio/anaconda3:latest` と表示されれば完了です。

### ダウンロードできたか確認する

```bash
docker images
```

以下のように `continuumio/anaconda3` が表示されればOKです：

```
REPOSITORY                TAG       IMAGE ID       CREATED        SIZE
continuumio/anaconda3     latest    xxxxxxxxxxxx   x weeks ago    3.5GB
```

---

## STEP 5: VS Code 拡張機能「Dev Containers」のインストール

勉強会後半のDev Containerパートで使用します。Git勉強会でインストールしたVS Codeに追加します。

### インストール手順

1. VS Codeを起動する
2. 左サイドバーの「拡張機能」アイコンをクリック（または `Ctrl + Shift + X`）
3. 検索欄に「Dev Containers」と入力
4. 「Dev Containers」（作者：**Microsoft**）をクリックして「インストール」
5. インストール後、VS Codeの左下に `><` のようなアイコンが追加されていれば完了

### インストールの確認

左下のステータスバーに `><` アイコンが表示されていればOKです。

---

## STEP 6: ハンズオン用リポジトリの取得（git pull）

ハンズオンで使用する `docker-compose.yml` や `Dockerfile`、サンプルコードはすべて **Git勉強会で使用した `git-practice-repo` リポジトリ** に含まれています。勉強会当日に最新の状態で利用できるよう、事前に `git pull` で取得しておきます。

### リポジトリを最新化する

Git勉強会で `git-practice-repo` をすでにクローン済みです。ターミナル（Git Bash または PowerShell）で以下を実行してください：

```bash
# Git勉強会でクローンした git-practice-repo フォルダに移動
# （クローン場所が異なる場合はそのパスに読み替えてください）
cd ~/Projects/git-practice-repo

# mainブランチに切り替え
git checkout main

# 最新の状態を取得
git pull origin main
```

> **まだクローンしていない場合：** 以下のコマンドでクローンしてください（URLはGit勉強会で案内されたものを使用）。
> ```bash
> cd ~/Projects
> git clone <git-practice-repoのURL>
> cd git-practice-repo
> ```

### ハンズオンで使うフォルダを確認する

`git pull` 後、リポジトリ内の `Docker勉強会/docker-jupyter/` フォルダにハンズオンで必要なファイルが揃っていることを確認します：

```bash
cd Docker勉強会/docker-jupyter
ls
```

以下のように `docker-compose.yml` と `notebooks/` フォルダが表示されればOKです：

```
docker-compose.yml
notebooks/
```

### ハンズオンで使うフォルダ構成

```
git-practice-repo/
└── Docker勉強会/
    ├── docker-jupyter/          ← JupyterLabハンズオン用フォルダ（ここでコマンドを実行する）
    │   ├── docker-compose.yml   ← 配布済み（git pullで取得）
    │   └── notebooks/           ← Notebookの保存先
    ├── my-project/              ← Dev Containerハンズオン用フォルダ
    │   ├── hello.py
    │   └── README.md
    ├── app.py                   ← Dockerfileハンズオン用サンプル
    └── Dockerfile               ← Dockerfileハンズオン用サンプル
```



---

## 事前準備 完了チェックリスト

勉強会当日までに、以下すべてにチェックが入るようにしてください。

- [ ] Docker Desktop がインストールされている
- [ ] タスクトレイのクジラアイコンが表示され、「Docker Desktop is running」になっている
- [ ] `docker --version` を実行してバージョンが表示される
- [ ] `docker run hello-world` を実行して「Hello from Docker!」が表示される
- [ ] `docker pull continuumio/anaconda3` が完了している
- [ ] `docker images` で `continuumio/anaconda3` が表示される
- [ ] VS CodeにDev Containers拡張機能がインストールされている（左下に`><`アイコンがある）
- [ ] `git-practice-repo` で `git pull origin main` を実行し、`Docker勉強会/docker-jupyter/docker-compose.yml` と `Docker勉強会/docker-jupyter/notebooks/` が存在することを確認した

---

## よくある質問（事前準備）

**Q: インストール中に「WSL2 installation is incomplete」というエラーが出ました**  
A: WSL2のLinuxカーネル更新プログラムが必要です。以下の手順で対処してください：
1. ブラウザで `https://aka.ms/wsl2kernel` を開く
2. ページ内の「x64 マシン用 WSL2 Linux カーネル更新プログラム パッケージ」をダウンロードしてインストール
3. インストール後、Docker Desktopを再起動

**Q: Docker Desktop は起動するがタスクトレイにアイコンが表示されません**  
A: タスクトレイの「∧」をクリックして隠れているアイコンを確認してください。それでも見当たらない場合はDocker Desktopを再起動してください。

**Q: `docker run hello-world` でエラーが出ます**  
A: Docker Desktopが完全に起動していない可能性があります。タスクトレイのクジラアイコンが「Docker Desktop is running」になっているか確認し、1〜2分待ってから再試行してください。

**Q: `docker pull continuumio/anaconda3` が途中で止まります**  
A: ダウンロードが中断された場合は、同じコマンドを再実行してください。途中から再開されます。社内ネットワークの場合、プロキシ設定が必要な場合があります。その場合は講師に相談してください。

**Q: 仮想化が有効になっているか確認する方法は？**  
A: タスクマネージャー（`Ctrl + Shift + Esc`）→「パフォーマンス」→「CPU」タブで「仮想化：有効」と表示されていれば問題ありません。

**Q: Macを使用しています。手順が違いますか？**  
A: Docker Desktopのインストール手順はMacでも同様です（`https://www.docker.com/products/docker-desktop/` からMac用をダウンロード）。操作コマンドは同じです。

**Q: Dev Containers拡張機能をインストールしたのに左下に`><`アイコンが出ません。**  
A: VS Codeを再起動してください。それでも表示されない場合は、拡張機能パネルで「Dev Containers」が有効になっているか確認してください。

---

*作成日：2026年*  
*対象：情報システム部 Docker勉強会 受講者*
