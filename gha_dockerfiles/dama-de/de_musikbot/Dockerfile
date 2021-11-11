FROM alpine:latest

RUN apk add python3 py3-pip py3-aiohttp

ADD main.py requirements.txt /bot/
ADD cogs/ /bot/cogs/
ADD util/ /bot/util/

VOLUME /data
ENV DATA_DIR=/data
WORKDIR /bot

RUN pip install -r requirements.txt
ENTRYPOINT python3 main.py