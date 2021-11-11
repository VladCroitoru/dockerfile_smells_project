FROM gogs/gogs:0.9.128

ENV VERSION=0.9.128

COPY docker-entrypoint.sh /entrypoint.sh
COPY app.ini .

ENTRYPOINT ["/entrypoint.sh"]

