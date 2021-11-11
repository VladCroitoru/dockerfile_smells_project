FROM postgres:9.5.2
MAINTAINER Devialab

RUN apt-get update && apt-get install -y python python-pip python-dev lzop pv daemontools

RUN pip install --upgrade pip
RUN pip install --upgrade six
RUN pip install --upgrade requests

RUN pip install wal-e

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME "/etc/wal-e/env"

COPY scripts/docker-entrypoint.sh /docker-entrypoint.sh

ADD scripts/fix-acl.sh /docker-entrypoint-initdb.d/
ADD scripts/setup-wale.sh /docker-entrypoint-initdb.d/

ADD crontab/wal-e /etc/cron.d/wal-e
RUN chmod 0644 /etc/cron.d/wal-e
RUN touch /var/log/cron.log