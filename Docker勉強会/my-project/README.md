# Dev Container ハンズオン用サンプル

第9章「ハンズオン：Dev Containerを使ってみる」で使用するサンプルプロジェクトです。

## ファイル構成

```
my-project/
├── .devcontainer/
│   └── devcontainer.json    ← Dev Container の設定（コメント付き）
├── hello.py                 ← 動作確認用スクリプト
└── README.md                ← このファイル
```

## 使い方

1. このフォルダ（`my-project/`）を VS Code で開く
2. 左下の `><` アイコン →「Reopen in Container」を選択
3. コンテナが起動したら、ターミナルで以下を実行

```bash
python hello.py
```

詳しい手順は `Docker勉強会_受講者用資料.md` の第9章を参照してください。
