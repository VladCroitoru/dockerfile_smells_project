FROM mohamnag/aws-cli
MAINTAINER Luca Mattivi <luca@smartdomotik.com>


RUN apt-get update \
    && apt-get install -yq --no-install-recommends mysql-client cron \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

# m h  dom mon dow
ENV BACKUP_CRON_SCHEDULE="0 * * * *"
ENV BACKUP_PRIORITY="ionice -c 3 nice -n 10"

# bucket/path/to/place/
ENV BACKUP_S3_BUCKET=
ENV AWS_DEFAULT_REGION=
ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=

ENV MYSQL_HOST=**None** \
	MYSQL_PORT=3306 \
	MYSQL_USER=root \
	MYSQL_PASSWORD=**None** \
	MYSQL_BACKUP_DIR=/var/backup/mysql

ADD crontab /etc/cron.d/backup-cron
ADD backup.sh /opt/backup.sh
ADD cron.sh /opt/cron.sh

RUN chmod 0644 /etc/cron.d/backup-cron
# Create the log file to be able to run tail
RUN touch /var/log/cron.log
RUN chmod +x /opt/*.sh


WORKDIR /opt/

CMD /opt/cron.sh
