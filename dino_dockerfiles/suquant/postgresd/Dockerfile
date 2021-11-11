FROM alpine:3.5
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN echo '@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories &&\
    apk add --no-cache postgresql postgresql-client postgresql-contrib \
    postgresql-libs postgresql-pglogical@testing sudo

ENV LANG=en_US.utf8 \
    LC_ALL=en_US.utf8 \
    LANGUAGE=en_US.utf8 \
    PGDATA=/var/lib/postgresql/data

VOLUME ["/var/lib/postgresql/data"]

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 5432