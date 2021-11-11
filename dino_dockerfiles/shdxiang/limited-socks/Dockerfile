FROM ubuntu:16.04

EXPOSE 8000/tcp

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:max-c-lv/shadowsocks-libev && \
  apt-get update && \
  apt-get install -y shadowsocks-libev iproute2 && \
  rm -rf /var/lib/apt/lists/*

ADD entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
