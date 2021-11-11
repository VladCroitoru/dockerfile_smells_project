FROM alpine:edge

RUN apk add --update bash wget tar gzip openssl

VOLUME ["/Sync"]
VOLUME ["/Config"]
VOLUME ["/syncthing"]
WORKDIR /Sync

EXPOSE 8080 22000
ADD start /start
ADD node_id /node_id
RUN chmod 0755 /start /node_id
CMD ["/start"]
