#!/bin/bash

dir=$(dirname $(realpath $0))

cd $dir
nohup python cron.py > /dev/null 2>&1 &

