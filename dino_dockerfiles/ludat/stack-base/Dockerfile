FROM debian:stable-slim

ENV LANG C.UTF-8

RUN apt update -y && apt install curl git -y

RUN curl -sSL https://get.haskellstack.org/ | sh
