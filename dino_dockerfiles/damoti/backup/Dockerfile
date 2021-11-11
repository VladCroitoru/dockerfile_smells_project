FROM postgres:10

ADD http://github.com/odise/go-cron/releases/download/v0.0.7/go-cron-linux.gz /
RUN gunzip -c go-cron-linux.gz > /usr/local/bin/go-cron && \
    chmod u+x /usr/local/bin/go-cron && \
    rm go-cron-linux.gz

ENV POSTGRES_PORT 5432
ENV POSTGRES_USER postgres
ENV POSTGRES_EXTRA_OPTS '-Z9'

ENV SCHEDULE '@hourly'
ENV BACKUP_DIR '/backups'
ENV BACKUP_KEEP_HOURLY 14
ENV BACKUP_KEEP_DAILY 60
ENV BACKUP_KEEP_WEEKLY 52
ENV BACKUP_KEEP_MONTHLY 24
ENV BACKUP_DAILY_HOUR_INTERVAL 4

COPY backup.sh /backup.sh

CMD go-cron -s "$SCHEDULE" -- /backup.sh
