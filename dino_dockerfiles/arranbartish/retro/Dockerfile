FROM node:boron

MAINTAINER Arran Bartish <arranbartish@hotmail.com>

ADD https://github.com/funretro/distributed/archive/master.tar.gz /Downloads/master.tar.gz

RUN tar -xzf /Downloads/master.tar.gz && \
    mv /distributed-master /retro && \
    npm i -g gulp && \
    cd /retro;npm install && \
    adduser --disabled-password --gecos "retro" --home /retro --no-create-home retro && \
    chown -R retro:retro /retro

EXPOSE 4000

WORKDIR /retro

USER retro

CMD ["gulp"]
