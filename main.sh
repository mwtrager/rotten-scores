#!/bin/bash
PATH="/usr/local/bin:/usr/local/sbin:~/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export LC_CTYPE="en_US.UTF-8"
pipenv run python rotten.py $1
