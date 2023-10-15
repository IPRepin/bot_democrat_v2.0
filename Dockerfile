FROM python:3.11-buster

WORKDIR /bot_democrat_v2
COPY requirements.txt /bot_democrat_v2
RUN pip install -r requirements.txt
COPY . /bot_democrat_v2