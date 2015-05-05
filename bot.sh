#!/bin/bash -l

cd ${PATH_TO_SHIBOT}

BOTPROC=`ps aux | grep shibot | grep python | grep -v grep | awk '{ print $2; }'`

if [ ! ${BOTPROC} ]
then
    nohup ./start.sh > /dev/null 2>&1 < /dev/null &
fi

cd -
