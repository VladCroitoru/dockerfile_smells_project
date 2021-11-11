FROM alpine

MAINTAINER upaver20, https://upaver20.com

VOLUME /MusicBot

RUN apk update \
 && apk add ca-certificates ffmpeg x264 python3 python3-dev libffi-dev libsodium-dev gdbm-dev libc-dev zlib-dev sqlite-dev tk-dev\
 && apk add --no-cache --virtual=.build-deps openssl-dev  git  alpine-sdk \
 && git clone https://github.com/upaver20/MusicBot.git /MusicBot -b master \
 && cd /MusicBot \
 && git checkout own_build\
 && python3 -m pip install --upgrade pip \
 && python3 -m pip install --upgrade -r requirements.txt\
 && apk del --purge .build-deps\
 && rm -rf ~/.cache/pip

WORKDIR /MusicBot

CMD python3 run.py
