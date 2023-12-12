# slack-ml-send

## Slack APIによるプログラミング　機械学習への応用編

Slack APIチュートリアル「NodeJSとSlack APIによるいまどきのネットワークプログラミング」の応用編として機械学習向けにアプリを公開する。

### メッセージを送信する

機械学習は学習対象とするデータセットから特徴を抽出して学習する過程にとても時間がかかる。このサンプルは、学習プログラムに埋め込んで、学習の途中経過や終了をSlackに通知することを意図する。

#### 必要なパッケージをインストールする

コマンドライン上で次のコマンドを起動し、依存するPythonパッケージをインストールする。

```bash
pip install -r requirements.txt
```

#### 環境変数を設定する

本アプリを起動するには環境変数の設定が必要である。env.tplファイルをenv.batバッチファイルとしてコピーし、以下の環境変数を定義する。

```bash
copy env.tpl env.bat
```

|  変数名  |  説明  |
| ---- | ---- |
|  SLACK_WEBHOOK_URL  | メッセージを送信するWebhook URL。対象Slackワークスペースのアプリ設定 > [Incoming Webhooks] |

#### テキストを送信する

- メッセージを送るサンプル。長時間かかる学習の途中経過あるいは処理が終了したことを通知するために用いる。
- 起動方法

```bash
env.bat
python send_message.py
```

### 更新履歴

- 2023-02-01 初版
