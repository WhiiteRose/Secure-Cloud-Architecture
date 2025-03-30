#!/bin/bash

set -xe

python3 app.py &
npm run dev &

wait -n
exit $?
