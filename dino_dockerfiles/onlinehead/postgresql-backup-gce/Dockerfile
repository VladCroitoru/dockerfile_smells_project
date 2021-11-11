# Here is a small container which you can use for backup/restore on GCE

FROM google/cloud-sdk:alpine

RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/community postgresql-client

# Set default timeout to 5 seconds
ENV PGCONNECT_TIMEOUT=5

ADD dump.sh /usr/bin/dump
ADD restore.sh /usr/bin/restore
RUN chmod +x /usr/bin/dump; chmod +x /usr/bin/restore



