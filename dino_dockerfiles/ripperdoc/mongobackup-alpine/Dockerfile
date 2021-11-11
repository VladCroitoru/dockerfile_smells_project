FROM alpine:edge
MAINTAINER Ripperdoc

# Adapted from https://github.com/rheosystems/dockerfiles/tree/master/mongodb-monitoring-agent

RUN apk --update add \
  bash \
  curl \
  cyrus-sasl-dev \
  logrotate && \
  rm -rf /var/cache/apk/*

# Put some libraries where expected for monitoring-agent (as we are on Alpine)
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 && ln -s /usr/lib/libsasl2.so.3 /usr/lib/libsasl2.so.2

RUN adduser -S mongodb-mms-agent
USER mongodb-mms-agent
WORKDIR /home/mongodb-mms-agent

# Get latest from https://mms.mongodb.com/settings/backup-agent
ENV MMS_VERSION 5.7.0.641-1
RUN curl -sSL https://cloud.mongodb.com/download/agent/backup/mongodb-mms-backup-agent-${MMS_VERSION}.linux_x86_64.tar.gz | tar -xz --strip-components=1

RUN chmod +w local.config

COPY entrypoint.sh .
ENTRYPOINT ["/home/mongodb-mms-agent/entrypoint.sh"]

CMD ["/home/mongodb-mms-agent/mongodb-mms-backup-agent"]