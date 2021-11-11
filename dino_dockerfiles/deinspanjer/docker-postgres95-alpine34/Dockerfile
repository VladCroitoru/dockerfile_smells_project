# vim:set ft=dockerfile:
FROM alpine:latest

ENV LANG en_US.utf8

RUN apk add --no-cache bash su-exec postgresql postgresql-contrib

RUN mkdir /docker-entrypoint-initdb.d

# make the sample config easier to munge (and "correct by default")
RUN sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!" /usr/share/postgresql/postgresql.conf.sample

RUN mkdir -p /run/postgresql /etc/postgresql && chown -R postgres /run/postgresql /etc/postgresql

ENV PGDATA /var/lib/postgresql/data
VOLUME /var/lib/postgresql/data
VOLUME /etc/postgresql

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]
