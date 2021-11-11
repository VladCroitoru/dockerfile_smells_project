FROM debian

RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends ca-certificates curl postgresql-client bzip2 && rm -rf /var/lib/apt/lists/* \
	&& apt-get purge -y --auto-remove ca-certificates && apt-get clean

ENV POSTGRES_DB **None**
ENV POSTGRES_HOST **None**
ENV POSTGRES_PORT 5432
ENV POSTGRES_USER **None**
ENV BACKUP_DIR '/backups'
ENV PGPASSWORD **None**
ENV SCHEDULE '@daily'

COPY autopgsqlbackup.sh go-cron ./

RUN chmod -R 777 autopgsqlbackup.sh go-cron


VOLUME /backups

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["exec ./go-cron -s \"$SCHEDULE\" -p 8686 -- /autopgsqlbackup.sh"]

HEALTHCHECK --interval=5m --timeout=5s \
  CMD curl -f http://localhost:8686/ || exit 1
