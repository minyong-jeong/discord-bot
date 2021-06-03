#!/bin/bash

dir=$(dirname $(realpath $0))

if [[ ! -d $dir/logs ]];then
    mkdir -p $dir/logs
fi

cd $dir
nohup python launcher.py > /dev/null 2>&1 &
