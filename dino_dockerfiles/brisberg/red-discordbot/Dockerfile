FROM ubuntu:16.04

MAINTAINER Brandon Risberg <brandon.risberg@gmail.com>

ENV APTLIST="git libav-tools libffi-dev libopus-dev libssl-dev python3.5-dev unzip ffmpeg wget ca-certificates build-essential"
ENV PIPLIST="git+https://github.com/Rapptz/discord.py@master#egg=discord.py[voice] imgurpython youtube_dl beautifulsoup4"

RUN apt-get update && apt-get install -y --no-install-recommends $APTLIST && apt-get clean
RUN ln -s /usr/bin/python3.5 /usr/bin/python

RUN wget --no-check-certificate -O /tmp/get-pip.py http://bootstrap.pypa.io/get-pip.py && python3.5 /tmp/get-pip.py

RUN pip install --trusted-host pypi.python.org $PIPLIST

COPY . /app
RUN chmod 0744 /app/entrypoint.sh
RUN mv /app/cogs /app/cogs_backup

VOLUME /app/cogs
VOLUME /app/data
WORKDIR /app

ENTRYPOINT ["/app/entrypoint.sh"]
