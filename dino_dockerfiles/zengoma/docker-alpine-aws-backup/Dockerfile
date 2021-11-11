FROM python:3.6-alpine

RUN apk update && apk add dcron wget rsync ca-certificates && rm -rf /var/cache/apk/*

RUN pip install --no-cache-dir awscli

RUN mkdir -p /var/log/cron && mkdir -m 0644 -p /var/spool/cron/crontabs && touch /var/log/cron/cron.log && mkdir -m 0644 -p /etc/cron.d

COPY /scripts/* /
RUN mkdir -p /backup

RUN chmod +x /docker-entrypoint.sh
RUN chmod +x /docker-cmd.sh


ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/docker-cmd.sh"]
