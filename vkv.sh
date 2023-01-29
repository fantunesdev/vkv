#!/bin/bash

cd /var/lib/vkv/
source .venv/bin/activate

python vkv/main.py $1 $2 $3
