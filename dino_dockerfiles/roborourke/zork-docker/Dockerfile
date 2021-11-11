FROM alpine:latest
MAINTAINER Robert O\'Rourke "rob@o-rourke.org"

RUN apk add --no-cache --update \
    build-base linux-headers \
    gcc make php5 php5-json php5-curl

COPY frotz /etc/frotz
WORKDIR /etc/frotz
RUN make dumb
RUN make install_dumb
RUN mkdir -p /var/www/frotz
RUN cp dfrotz /var/www/frotz/

RUN mkdir /var/www/frotz/saves
RUN mkdir /var/www/frotz/streams
RUN mkdir /var/www/frotz/data
COPY restful-frotz /var/www/frotz/rest
COPY data/ZORK1.DAT /var/www/frotz/data/
COPY data/ZORK2.DAT /var/www/frotz/data/
COPY data/ZORK3.DAT /var/www/frotz/data/

VOLUME /var/www/frotz/saves
VOLUME /var/www/frotz/streams

WORKDIR /var/www/frotz/rest
EXPOSE 80
CMD php -S 0.0.0.0:80
