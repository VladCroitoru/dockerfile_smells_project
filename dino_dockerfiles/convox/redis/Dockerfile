FROM gliderlabs/alpine:3.4

RUN apk add --no-cache curl redis

RUN curl -o /usr/local/bin/gosu -sSL "https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64"
RUN chmod +x /usr/local/bin/gosu

# convox assembles these into a URL during `convox start`
ENV LINK_SCHEME redis
ENV LINK_PATH /0

RUN mkdir /data && chown nobody:nobody /data
VOLUME /data
WORKDIR /data

COPY docker-entrypoint.sh /

RUN apk del curl

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 6379
CMD ["redis-server", "/tmp/redis.conf"]
