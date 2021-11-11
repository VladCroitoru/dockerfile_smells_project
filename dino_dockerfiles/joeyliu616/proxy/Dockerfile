#
# Dockerfile for privoxy
#
FROM alpine:edge
MAINTAINER joey <joeyliu616@live.cn>

RUN set -xe \
    && apk add -U privoxy putty expect openssh-client curl \
    && curl -sSL https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64 > /usr/sbin/gosu \
    && chmod +x /usr/sbin/gosu \
#    && apk del curl \
    && rm -rf /var/cache/apk/*

ENV Username ""
ENV Password ""
ENV Server ""

ADD config/config /etc/privoxy/config
COPY scripts scripts

WORKDIR /scripts

VOLUME /etc/privoxy

EXPOSE 8888
EXPOSE 8118

CMD ["/bin/sh", "start.sh"] 
