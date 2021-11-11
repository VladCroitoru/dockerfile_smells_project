FROM frolvlad/alpine-glibc:latest
MAINTAINER François ALLAIS <francois.allais@hotmail.com>

RUN apk add --update git \
    && mkdir /data /app \
    && cd /app \
    && git clone https://github.com/nmcclain/glauth \
    && cp /app/glauth/bin/glauth64 /app/glauth64 \
    && rm -Rf glauth/

EXPOSE 389
VOLUME [ "/data" ]
CMD [ "/app/glauth64", "-c", "/data/glauth.cfg" ]
