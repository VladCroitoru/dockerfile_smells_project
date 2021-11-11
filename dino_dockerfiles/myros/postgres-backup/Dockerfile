FROM  postgres:10.2-alpine
LABEL maintainer="Myros <myros.net@gmail.com>"

RUN set -ex \
    \
		&& apk add --update --no-cache --virtual .fetch-deps \
        ca-certificates \
  && apk add --no-cache --virtual .fetch-deps \
	   curl dcron wget rsync ca-certificates \
  && curl -L https://github.com/odise/go-cron/releases/download/v0.0.7/go-cron-linux.gz | zcat > /usr/local/bin/go-cron \
	&& chmod a+x /usr/local/bin/go-cron \
	&& rm -rf /var/cache/apk/*

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install awscli \
  && rm -rf /var/cache/apk/*

ENV \
    S3_ACCESS_KEY \
    S3_SECRET_KEY \
    S3_REGION \
    S3_BUCKET \
    PG_HOST \
    PG_DATABASE \
    PG_USER \
    PG_PASSWORD \
    POSTGRES_EXTRA_OPTS \
    SCHEDULE=@daily \
    BACKUP_DIR \
    BACKUP_KEEP_DAYS \
    BACKUP_KEEP_WEEKS \
    BACKUP_KEEP_MONTHS

VOLUME /backups

ADD s3cfg /root/.s3cfg

# entrypoint
ADD entrypoint.sh /entrypoint.sh

ADD run.sh run.sh
ADD backup.sh backup.sh
ADD restore.sh restore.sh
ADD restore.py restore.py

ENTRYPOINT ["/bin/sh", "-c"]

CMD ["exec /usr/local/bin/go-cron -s \"$SCHEDULE\" -p 80 -- /backup.sh"]

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost/ || exit 1
