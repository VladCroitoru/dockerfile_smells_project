FROM python:3.7

MAINTAINER Nick "wasserball@me.com"

ENV SPEEDTEST_CLI_VERSION 2.1.1

RUN apt-get update && \
    apt-get upgrade -y

RUN pip install speedtest-cli==$SPEEDTEST_CLI_VERSION
RUN pip install matplotlib

# install x11
RUN apt-get update &&\
    apt-get install -y xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic x11-apps clang libdbus-1-dev libgtk2.0-dev libnotify-dev libgnome-keyring-dev libgconf2-dev libasound2-dev libcap-dev libcups2-dev libxtst-dev libxss1 libnss3-dev gcc-multilib g++-multilib


RUN mkdir /data
COPY entrypoint.sh /
COPY plot.py /

CMD bash /entrypoint.sh