FROM alpine:3.6
MAINTAINER Tomas Janecek

RUN apk add --no-cache \
      mysql=10.1.26-r0 \
      mysql-client=10.1.26-r0 \
   && rm -rf /var/lib/mysql \
   && ln -s /app/data/mysql /var/lib/mysql

COPY start.sh /app/start.sh

WORKDIR /app/

VOLUME /app/data

USER nobody

CMD ["/app/start.sh"]
