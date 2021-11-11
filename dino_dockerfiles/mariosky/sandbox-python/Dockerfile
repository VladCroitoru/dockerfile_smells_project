FROM alpine:3.6

ENV ALPINE_VERSION=3.6


RUN apk update && apk --update  add git python3

RUN pip3 install redis==2.10.6
RUN pip3 install tap.py
RUN git clone https://github.com/mariosky/sandbox.git /home/sandbox



