FROM golang:alpine


RUN apk update && apk --update  add git python py-pip

RUN pip install redis tap.py
RUN git clone https://github.com/mariosky/sandbox.git /home/sandbox

