FROM debian:jessie
MAINTAINER William Blankenship <william.jblankenship@gmail.com>

RUN apt-get update; \
    apt-get install -y --force-yes \
                    cowsay

ENV PATH /usr/games:$PATH

cmd ["cowsay","What does the cowsay?"]
