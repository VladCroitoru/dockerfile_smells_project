FROM mohamnag/aws-cli
MAINTAINER Luca Mattivi <luca@smartdomotik.com>

# change these to fit your need
RUN apt-get update -q && apt-get install cron --yes

# m h  dom mon dow
ENV BACKUP_CRON_SCHEDULE="* * * * *"

ENV BACKUP_TGT_DIR=/backup/
ENV BACKUP_SRC_DIR=/data/
ENV BACKUP_FILE_NAME='host_volumes'

# bucket/path/to/place/
ENV BACKUP_S3_BUCKET=
ENV AWS_DEFAULT_REGION=
ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=

ADD crontab /etc/cron.d/backup-cron
ADD backup.sh /opt/backup.sh
ADD restore.sh /opt/restore.sh
ADD cron.sh /opt/cron.sh

RUN chmod 0644 /etc/cron.d/backup-cron
# Create the log file to be able to run tail
RUN touch /var/log/cron.log
RUN chmod +x /opt/*.sh

VOLUME $BACKUP_TGT_DIR
VOLUME $BACKUP_SRC_DIR

WORKDIR /opt/

CMD /opt/cron.sh
