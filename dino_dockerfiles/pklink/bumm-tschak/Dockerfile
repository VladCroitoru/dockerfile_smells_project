FROM node:latest
MAINTAINER Pierre Klink <docker@klink.xyz>

WORKDIR /root

ADD https://github.com/mholt/caddy/releases/download/v0.8.2/caddy_linux_amd64.tar.gz /root/caddy_linux_amd64.tar.gz
COPY . /root

RUN tar xzf caddy_linux_amd64.tar.gz \
    && tar -xzf caddy_linux_amd64.tar.gz && rm caddy_linux_amd64.tar.gz \
    && npm install \
    && node_modules/.bin/webpack

EXPOSE 2015

ENTRYPOINT ["./caddy"]
