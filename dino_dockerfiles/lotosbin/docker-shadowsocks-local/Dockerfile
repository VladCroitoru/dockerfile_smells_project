FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y python-pip libsodium18
RUN pip install --upgrade pip
RUN pip install https://github.com/shadowsocks/shadowsocks/archive/2.9.1.zip

ENTRYPOINT ["sslocal"]

