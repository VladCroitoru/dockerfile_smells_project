FROM alpine:3.4

RUN apk add --no-cache curl bind-tools

ADD update_dns.sh /bin/

ADD crontab /var/spool/cron/crontabs/root

RUN mkdir /var/cache/dns_updater && chmod +x /bin/update_dns.sh

CMD /bin/update_dns.sh && crond -l 2 -f
