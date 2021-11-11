FROM ubuntu:xenial
MAINTAINER Marius Rennmann <marius@dontmind.me>

RUN apt-get update && apt-get install -y s3cmd cron

ADD /scripts /dockup/
RUN chmod 755 /dockup/*.sh

ENV S3_BUCKET_NAME container-backup
ENV AWS_ACCESS_KEY_ID **DefineMe**
ENV AWS_SECRET_ACCESS_KEY **DefineMe**
ENV S3_HOST s3.amazonaws.com
ENV S3_HOST_BUCKET %(bucket)s.s3.amazonaws.com
ENV AWS_DEFAULT_REGION us-east-1
ENV S3_SSL true
ENV PATHS_TO_BACKUP auto
ENV BACKUP_NAME backup
ENV RESTORE false
ENV RESTORE_TAR_OPTION --preserve-permissions
ENV NOTIFY_BACKUP_SUCCESS false
ENV NOTIFY_BACKUP_FAILURE false
ENV BACKUP_TAR_TRIES 5
ENV BACKUP_TAR_RETRY_SLEEP 30

WORKDIR /dockup
CMD ["./run.sh"]
