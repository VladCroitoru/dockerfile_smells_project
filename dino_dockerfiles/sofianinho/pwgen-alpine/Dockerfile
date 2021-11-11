FROM gliderlabs/alpine:3.3
MAINTAINER sofiane.imadali@orange.com

RUN apk add --update pwgen && \
    rm -rf /var/cache/apk/* /tmp/* /var/tmp/* 
    
USER nobody
ENTRYPOINT ["pwgen"]
