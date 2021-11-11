FROM registry.cn-hangzhou.aliyuncs.com/firewarm/apps:alpine-base-3.4

MAINTAINER Lighting <liuyg@liuyingguang.cn>

ENV LEANOTE_VERSION=2.1

RUN mkdir -p /usr/local/src \
  && cd /usr/local/src \
  && curl -sSL https://nchc.dl.sourceforge.net/project/leanote-bin/${LEANOTE_VERSION}/leanote-linux-amd64-v${LEANOTE_VERSION}.bin.tar.gz | tar -zx \
  && apk del make gcc g++ python linux-headers paxctl \
  && chmod +x /usr/local/src/leanote/bin/run.sh

EXPOSE 9000
CMD ["/usr/local/src/leanote/bin/run.sh"]