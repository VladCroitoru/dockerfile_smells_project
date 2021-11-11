FROM alpine:3.6

ENV VER=0.28.0 CERT_PEM=none KEY_PEM=none

RUN \
    apk add --no-cache --virtual  curl \
    && mkdir -m 777 /gsnova \
    && cd /gsnova \
    && curl -fSL https://github.com/yinqiwen/gsnova/releases/download/v$VER/gsnova_server_linux_amd64-v$VER.tar.bz2 | tar xj  \
    && rm -rf server.json \
    && rm -rf gsnova_server_linux_amd64-v$VER.tar.bz2 \
    && chgrp -R 0 /gsnova \
    && chmod -R g+rwX /gsnova 
    
ADD server.json /gsnova/server.json    
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh 
ENTRYPOINT  /entrypoint.sh 

EXPOSE 8080 8088
