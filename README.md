# slack-ml-send

## Slack APIによるプログラミング　機械学習への応用編

Slack APIチュートリアル「NodeJSとSlack APIによるいまどきのネットワークプログラミング」の応用編として機械学習向けにアプリを公開する。

### メッセージを送信する

機械学習は学習対象とするデータセットから特徴を抽出して学習する過程にとても時間がかかる。このサンプルは、学習プログラムに埋め込んで、学習の途中経過や終了をSlackに通知することを意図する。

#### 必要なライブラリをインストールする

>$ pip install -r requirements.txt

#### 環境変数を設定する

- ファイルenv.tpl内のSLACK_WEBHOOK_URLに該当するURLを設定する
- env.tplをenv.batに名前を変え、バッチを実行する
  >$ ren env.tpl env.bat
  >
  >$ env.bat

#### テキストを送信する

- メッセージを送るサンプル。長時間かかる学習の途中経過あるいは処理が終了したことを通知するために用いる。
- 起動方法

  >$ python send_message.py
