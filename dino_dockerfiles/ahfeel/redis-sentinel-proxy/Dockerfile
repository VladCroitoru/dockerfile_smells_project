FROM golang:onbuild

MAINTAINER Jérémie BORDIER <jeremie.bordier@gmail.com>

RUN mkdir /app
ADD main.go /app/
WORKDIR /app
RUN go build -o redis-sentinel-proxy . && mv redis-sentinel-proxy /usr/local/bin/redis-sentinel-proxy

COPY docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["redis-sentinel-proxy"]