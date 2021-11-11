FROM miniers/alpine-nginx-node
MAINTAINER miniers

ADD conf/node /node

RUN cd /node && \
    npm i 

ADD conf/nginx /etc/nginx

WORKDIR /node

ADD conf/services.d/node /etc/services.d/node