FROM alpine

RUN apk --update add logrotate
ENV STATE_FILE /opt/logs/logrotate.status
RUN echo "*/5 * * * * /usr/sbin/logrotate --state $STATE_FILE /opt/etc/logrotate.conf" >> /etc/crontabs/root

CMD ["crond", "-f"]