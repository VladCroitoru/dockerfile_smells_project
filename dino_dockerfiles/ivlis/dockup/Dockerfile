FROM alpine:3.4
MAINTAINER Simon Templer <simon@wetransform.to> Ivan Lisenkov <ivan@ivlis.com>

# RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories  && \
#     apk add --update --no-cache curl awscli@testing bash grep
# RUN apt-get update && apt-get install -y python-pip curl && pip install awscli

RUN apk add --update --no-cache curl bash grep python py-pip ca-certificates tzdata tar gnupg && \
    pip install awscli


ADD /scripts /dockup/
RUN chmod 755 /dockup/*.sh

ENV S3_BUCKET_NAME docker-backups.example.com
ENV AWS_ACCESS_KEY_ID **DefineMe**
ENV AWS_SECRET_ACCESS_KEY **DefineMe**
ENV AWS_DEFAULT_REGION us-east-1
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
