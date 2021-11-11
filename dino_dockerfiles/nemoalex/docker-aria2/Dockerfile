FROM alpine:edge
MAINTAINER Nemo Alex <zhhjchina@gmail.com>

RUN set -xe \
    && apk add --no-cache aria2 \
    && aria2c https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64 -o /usr/local/bin/gosu \
    && chmod +x /usr/local/bin/gosu \
    && adduser -D aria2 \
    && mkdir /home/aria2/downloads

VOLUME /home/aria2/downloads /etc/aria2

EXPOSE 6800
CMD set -xe \
    && chown -R aria2:aria2 /home/aria2 \
    && chown -R aria2:aria2 /etc/aria2 \
    && gosu aria2 aria2c --conf-path=/etc/aria2/aria2.conf \
                         --rpc-listen-port=6800 \
                         --dir=/home/aria2/downloads
