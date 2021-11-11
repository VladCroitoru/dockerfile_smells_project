#
#Dockerfile for aria2
#
FROM alpine
LABEL maintainer="lunksana <lunksana@gmail.com>"
RUN apk update && \
    apk add aria2 && \
    apk add wget && \
    rm /var/cache/apk/* && \
    mkdir -p /aria2/conf && \
    mkdir /aria2/downloads
VOLUME [ "/aria2/conf","/aria2/downloads" ]

ADD start.sh /aria2
ADD aria2.conf /aria2
ADD dht.dat /aria2
RUN chmod +x /aria2/start.sh
EXPOSE 6800
ENV SECRET=password
CMD set -xe &&\
    /aria2/start.sh