FROM node:14-buster

ENV VERSION=1.14.0

RUN mkdir p /srv/reva && \
    cd /srv/reva && \
    wget -O revad https://github.com/cs3org/reva/releases/download/v${VERSION}/revad_v${VERSION}_linux_amd64  && \
    chmod +x revad && \
    wget -O reva https://github.com/cs3org/reva/releases/download/v${VERSION}/reva_v${VERSION}_linux_amd64 && \
    chmod +x reva
