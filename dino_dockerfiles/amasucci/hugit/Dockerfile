FROM alpine:latest
MAINTAINER Antonio Masucci <eng.masucci@gmail.com>

ADD https://github.com/gohugoio/hugo/releases/download/v0.24.1/hugo_0.24.1_Linux-64bit.tar.gz /tmp/hugo.tar.gz

RUN tar -xf /tmp/hugo.tar.gz -C /tmp &&     mkdir -p /usr/local/sbin &&     mv /tmp/hugo /usr/local/sbin/hugo &&     rm -rf /tmp/hugo.tar.gz

VOLUME /site

WORKDIR /site

COPY ./entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 80
