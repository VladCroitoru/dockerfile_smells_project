FROM alpine:3.4
MAINTAINER Chris Schmich <schmch@gmail.com>
RUN apk add --no-cache ruby ruby-json xz jq ca-certificates tzdata
RUN cp /usr/share/zoneinfo/US/Central /etc/localtime \
 && echo "US/Central" > /etc/timezone
COPY crontab /var/spool/cron/crontabs/root
COPY worker /srv/scry
ENTRYPOINT ["/usr/sbin/crond", "-f"]
