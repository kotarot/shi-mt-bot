#!/bin/bash

PIDS=(`ps aux | grep shibot | grep python | grep -v grep | awk '{ print $2; }'`)
echo ${PIDS}
