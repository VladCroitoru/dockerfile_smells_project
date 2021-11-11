FROM ubuntu:xenial
MAINTAINER Simon Templer <simon@wetransform.to>

RUN apt-get update && apt-get upgrade -y && apt-get install -y python-pip curl cron && pip install awscli

ADD /scripts /dockup/
RUN chmod 755 /dockup/*.sh

ENV S3_BUCKET_NAME docker-backups.example.com
# Use ECS Task role
# ENV AWS_ACCESS_KEY_ID **DefineMe**
# ENV AWS_SECRET_ACCESS_KEY **DefineMe**
ENV AWS_DEFAULT_REGION us-east-1
ENV PATHS_TO_BACKUP auto
ENV CONTENT_ONLY false
ENV BACKUP_NAME backup
ENV RESTORE false
ENV RESTORE_TAR_OPTION --preserve-permissions
ENV NOTIFY_BACKUP_SUCCESS false
ENV NOTIFY_BACKUP_FAILURE false
ENV BACKUP_TAR_TRIES 5
ENV BACKUP_TAR_RETRY_SLEEP 30

WORKDIR /dockup
ENV WORKDIR /dockup

CMD ["./run.sh"]
