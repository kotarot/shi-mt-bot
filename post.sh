#!/bin/bash -l

cd ${PATH_TO_SHIBOT}

if [ $# -ne 2 ]; then
    /usr/local/bin/python3 bot/post.py
else
    /usr/local/bin/python3 bot/post.py $1 $2
fi

cd -
