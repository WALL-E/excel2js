#!/bin/bash

cd `dirname $0`

command node -v 1>/dev/null 2>/dev/null
ret=$?
if test $ret -ne 0
then
    echo "需要安装nodejs"
    exit 1
fi


../excel2js.py ../cases.xlsx ../cases.js
node ./test.js
