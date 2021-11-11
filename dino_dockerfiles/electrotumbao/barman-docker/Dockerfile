FROM postgres:latest

RUN apt-get update \
  && apt-get install -y --no-install-recommends barman gettext-base \
  && rm -rf /var/lib/apt/lists/*

ENV \
	BARMAN_DATA_DIR=/var/lib/barman \
  BARMAN_LOG_LEVEL=INFO \
  BARMAN_CRON_SCHEDULE="* * * * *" \
  BARMAN_BACKUP_SCHEDULE="0 1 * * *" \
  BARMAN_RECEIVE_WAL_TIMEOUT=10 \
  BARMAN_BACKUP_RETENTION_DAYS=30 \
  BARMAN_MINIMUM_REDUNDANCY=0 \
    DB_BACKUP_METHOD=postgres \
    DB_HOST=pg \
    DB_PORT=5432 \
    DB_SUPERUSER=postgres \
    DB_SUPERUSER_PASSWORD=postgres \
    DB_NAME=postgres \
    DB_REPLICATION_USER=standby \
    DB_REPLICATION_PASSWORD=standby \
    DB_SLOT_NAME=barman

COPY barman.conf.template /etc/barman.conf.template

# https://sourceforge.net/p/pgbarman/tickets/88/
RUN sed -i '/def main():/a \ \ \ \ reload(sys);sys.setdefaultencoding("utf8")' /usr/lib/python2.7/dist-packages/barman/cli.py

VOLUME ${BARMAN_DATA_DIR}
WORKDIR ${BARMAN_DATA_DIR}

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["cron", "-l", "0",  "-f"]
