FROM luafan/webase

ENV REMOTE_HOST 127.0.0.1
ENV REMOTE_PORT 10000

ENV KEEPALIVE_DELAY 10
ENV PEER_TIMEOUT 600
ENV UDP_PACKAGE_TIMEOUT 3
ENV UDP_WAITING_COUNT 10

ENV DROP_PACKAGE_OUTSIDE_WINDOW false

ENV NAT_NAME docker

ENV SERVER_ENABLED false
ENV CLIENT_ENABLED true

ENV SERVER_PORT 10000

COPY *.lua /root/
COPY config /root/config

COPY web /root/web
COPY handle /root/handle
COPY service /root/service
COPY mapping /root/mapping
COPY database /root/database
