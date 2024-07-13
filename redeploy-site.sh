#!/bin/bash

pkill -f tmux

cd /root/MLH_Portfolio 

git fetch && git reset origin/main --hard

pip install -r requirements.txt

source python3-virtualenv/bin/activate

tmux new-session -d -s flask-server "cd /root/MLH_Portfolio && flask run --host=0.0.0.0"

