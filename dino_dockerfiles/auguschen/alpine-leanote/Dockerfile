FROM alpine

MAINTAINER Chen Augus <tianhao.chen@gmail.com>

RUN apk update && rm -rf /tmp/leanote.tar.gz && rm -rf /opt/leanote && mkdir -p /tmp && cd /tmp && wget -c -O leanote.tar.gz "http://jaist.dl.sourceforge.net/project/leanote-bin/2.2.1/leanote-linux-amd64-v2.2.1.bin.tar.gz" && mkdir -p /opt && cd /opt && tar -xzf /tmp/leanote.tar.gz && rm -rf /tmp/leanote.tar.gz

EXPOSE 9000

ENTRYPOINT sh /opt/leanote/bin/run.sh
