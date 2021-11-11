FROM alpine:edge
MAINTAINER Riad Vargas de Oliveira riad@leafhost.com.br

RUN mkdir /web /web/data /web/log /web/conf /run/nginx /tmp/nginx

RUN apk add --update nginx ca-certificates # Installing nginx and ca-certificates to support SSL

RUN rm -rf /var/cache/apk/* # Minimizing image size by excluding cache

ADD seed/nginx.conf /web/conf/nginx.conf
ADD seed/bolt.sh /
RUN chmod +x /bolt.sh


EXPOSE 80
VOLUME ["/web"]

CMD ["/bolt.sh"]
