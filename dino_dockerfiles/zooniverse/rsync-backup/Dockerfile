FROM alpine

RUN apk add --no-cache rsync

COPY backup.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/backup.sh

ENTRYPOINT [ "/usr/local/bin/backup.sh" ]
