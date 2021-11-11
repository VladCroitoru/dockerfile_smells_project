FROM gliderlabs/alpine:3.4

RUN apk --update add \
  ca-certificates \
  bash \
  jq \
  curl

ADD scripts/install_fly.sh install_fly.sh
RUN ./install_fly.sh

ADD assets/ /opt/resource/
RUN chmod +x /opt/resource/*
