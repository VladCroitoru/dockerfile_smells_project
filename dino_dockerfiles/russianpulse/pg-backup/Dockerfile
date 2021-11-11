FROM debian:jessie

RUN apt-get update && apt-get install -y \
  cron \
  postgresql-client \
  duplicity \
  ncftp

RUN mkdir /backup
RUN touch /var/log/backup.log
ADD ./bin/backup /etc/cron.daily/
RUN chmod +x /etc/cron.daily/backup

ADD ./bin/backup /bin/backup
ADD ./bin/restore /bin/restore

RUN mkdir /restore

CMD tail -f /var/log/backup.log
