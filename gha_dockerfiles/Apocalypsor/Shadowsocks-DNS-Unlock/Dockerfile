FROM --platform=$BUILDPLATFORM teddysun/shadowsocks-libev:latest

ARG UPSTEAM_HASH=1c20e0b8efe4068816881dab6b7d28647672e98d60a80e5e0d5dee62a92ebade

COPY config.example.json /etc/shadowsocks-libev/config.json
COPY entrypoint.sh /entrypoint.sh

RUN apk update \
    && apk --no-cache add dnsmasq curl \
    && echo -e 'server=1.1.1.1\nserver=8.8.8.8\nserver=208.67.222.222\nconf-dir=/etc/dnsmasq.d' > /etc/dnsmasq.conf \
    && chmod +x /entrypoint.sh

ENV NETFLIX_DNS="" 
ENV DISNEYPLUS_DNS=""
ENV PRIMEVIDEO_DNS=""
ENV YOUTUBE_DNS=""

ENV BILIBILI_DNS=""

ENTRYPOINT ["/entrypoint.sh"]
