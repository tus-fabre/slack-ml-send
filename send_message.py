#!/usr/bin/env python
# coding: utf-8
#
# [FILE] send_message.py
#
# [DESCRIPTION]
#  機械学習の学習完了をslackに通知するサンプル
#  学習を実行するプログラムの終了箇所にコードを付与する
#
# [NOTES]
#  Incoming Webhookアプリを使ってメッセージを送信する
#  対象となるチャネルは#general、そのURLは環境変数SLACK_WEBHOOK_URLに定義
#
import os, sys
import slackweb

webhook_url=os.environ.get("SLACK_WEBHOOK_URL")
if webhook_url == None:
    print("環境変数が設定されていません")
    sys.exit()

slack = slackweb.Slack(url=webhook_url)
slack.notify(text="学習が終了しました")

#
# END OF FILE
#