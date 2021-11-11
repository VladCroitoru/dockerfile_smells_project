FROM sdurrheimer/alpine-glibc
MAINTAINER Thibault NORMAND <me@zenithar.org>

ADD https://dl.minio.io/server/minio/release/linux-amd64/minio /usr/bin/minio
ADD https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 /usr/bin/gosu
ADD entrypoint.sh .

RUN chmod +x /usr/bin/minio \
    && chmod +x /usr/bin/gosu \
    && chmod +x /entrypoint.sh \
    && addgroup minio \
    && adduser -s /bin/false -G minio -S -D minio

ENTRYPOINT  ["/entrypoint.sh"]
VOLUME      ["/data"]
EXPOSE      9000
CMD         ["server","/data"]
