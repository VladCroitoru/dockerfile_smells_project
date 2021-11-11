FROM alpine:3.14
RUN apk add py3-pip mongodb-tools && pip3 install awscli

WORKDIR /app

COPY backup.sh /app/backup.sh
COPY entrypoint.sh /app/start.sh

RUN chmod 0644 /app/backup.sh
RUN chmod 0755 /app/start.sh

RUN touch /var/log/cron.log

CMD sh /app/start.sh