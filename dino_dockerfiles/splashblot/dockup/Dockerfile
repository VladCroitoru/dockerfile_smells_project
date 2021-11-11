FROM alpine:3.4
MAINTAINER Simon Templer <simon@wetransform.to> Ivan Lisenkov <ivan@ivlis.com>

RUN apk update && apk upgrade --no-cache && apk add --update --no-cache curl bash grep python py-pip ca-certificates tzdata tar gnupg && \
    pip install --upgrade pip && \
    pip install awscli && \
    rm -rf /var/cache/apk/*

ADD /scripts /dockup/
RUN chmod 755 /dockup/*.sh

ENV S3_BUCKET_NAME docker-backups.example.com
ENV AWS_ACCESS_KEY_ID **DefineMe**
ENV AWS_SECRET_ACCESS_KEY **DefineMe**
ENV AWS_USE_SERVICE_TASK_ROLE false
ENV AWS_DEFAULT_REGION eu-central-1
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
