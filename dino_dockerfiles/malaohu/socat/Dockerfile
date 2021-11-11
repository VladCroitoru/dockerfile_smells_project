FROM debian:jessie
MAINTAINER malaohu <tua@live.cn>

RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["socat"]
