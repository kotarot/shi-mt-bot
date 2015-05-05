#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
しおり修論大好きbot ランダムポスト
"""

import csv
import sys
import os
import random

# Python Twitter Tools
# https://github.com/sixohsix/twitter
from twitter import *


# Configurations from 環境変数
CONSUMER_KEY        = os.environ.get("SHIBOT_CONSUMER_KEY")
CONSUMER_SECRET     = os.environ.get("SHIBOT_CONSUMER_SECRET")
ACCESS_TOKEN        = os.environ.get("SHIBOT_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("SHIBOT_ACCESS_TOKEN_SECRET")


# ポストする
def do_post(t, text):
    if text != "":
        print("status: ", text)
        try:
            t.statuses.update(status=text)
        except TwitterError as e:
            print("[Exception] TwitterError!")
            print(e)
        except TwitterHTTPError as e:
            print("[Exception] TwitterHTTPError!")
            print(e)


if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)

    # オプション
    print("[Info] argvs: ", argvs)
    print("[Info] argc: ", argc)
    if 2 < argc:
        mode_appointed = True
        hour = argvs[1]
        minute = argvs[2]
    else:
        mode_appointed = False
    print("[Info] mode_appointed: ", mode_appointed)

    # CSV読み込み
    random_posts = []
    appointed_texts = []
    with open(os.environ.get("PATH_TO_SHIBOT") + "/csv/posts.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for line in reader:
            if line[1] == "-1" and line[2] == "-1":
                random_posts.append(line[3])
            elif mode_appointed and line[1] == hour and line[2] == minute:
                appointed_texts.append(line[3])
    print("random_posts: ", random_posts)

    # ポスト内容決定
    post_texts = []
    if mode_appointed:
        post_texts = appointed_texts
    if not mode_appointed:
        post_texts.append(random.choice(random_posts))
    print("post_texts: ", post_texts)

    # Twitter OAuth 認証
    auth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    # REST
    t = Twitter(auth=auth)

    for text in post_texts:
        do_post(t, text)
