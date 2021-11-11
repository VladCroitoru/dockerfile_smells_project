FROM alpine:3.6

MAINTAINER Ianus IT GmbH <info@ianus-it.de>

RUN apk add --update-cache libressl2.5-libcrypto &&\
    apk add --update-cache --repository http://dl-3.alpinelinux.org/alpine/v3.6/community/ prosody &&\
    rm -rf /var/cache/apk/*
    
COPY files/defaults/ /defaults/    
COPY files/start.sh /start.sh

RUN chmod +x /start.sh

CMD ["/start.sh"]
