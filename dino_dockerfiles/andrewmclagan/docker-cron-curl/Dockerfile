FROM alpine:3.6

RUN apk --no-cache add curl bash

RUN mkdir -p /var/log/cron \
    && touch /var/log/cron/cron.log \
    && mkdir -m 0644 -p /etc/cron.d

ADD ./config/schedule /etc/crontabs/root

CMD bash -c "crond -L /var/log/cron/cron.log && tail -F /var/log/cron/cron.log"
