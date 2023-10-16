#!/bin/bash
cd bot_democrat_v2.0
git pull origin master
source venv/bin/activate
sudo docker-compose restart