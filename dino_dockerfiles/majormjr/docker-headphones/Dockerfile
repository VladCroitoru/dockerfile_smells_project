FROM alpine

RUN apk add --update python git wget

COPY docker-entrypoint.sh /
RUN chmod 775 /docker-entrypoint.sh

RUN adduser -S -s /bin/sh -u 10000 headphones

VOLUME /downloads
VOLUME /headphones
VOLUME /torrents

EXPOSE 8081

ENTRYPOINT ["/docker-entrypoint.sh"]
