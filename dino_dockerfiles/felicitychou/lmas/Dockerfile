FROM ubuntu:16.04
MAINTAINER felicitychou<felicitychou@hotmail.com>

RUN apt-get update && apt-get install -y \
tcpdump \
strace \
ltrace \
python \
&& apt-get clean -y \
&& apt-get autoremove -y \
&& rm -rf /var/lib/apt/lists/*
