FROM ubuntu:16.04

RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \
    apt-get update && \
    apt-get install cron bzip2 s3cmd -y && \
    apt-get install mongodb-org-tools --allow-unauthenticated && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /backups

ENV BACKUP_TIME 0 3 * * *

COPY docker-entrypoint.sh /entrypoint.sh
COPY backup /bin/

ENTRYPOINT ["/entrypoint.sh"]

CMD ["cron", "-f"]

