FROM alpine

RUN apk add --update \
    mysql-client \
    bash \
&& rm -rf /var/cache/apk/*

ENTRYPOINT ["/usr/bin/mysqldump"]
