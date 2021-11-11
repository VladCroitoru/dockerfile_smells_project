FROM alpine
MAINTAINER ServiceRocket Engineering

RUN apk add --update wget curl duply tzdata \
      && cp /usr/share/zoneinfo/Asia/Kuala_Lumpur /etc/localtime \
      && echo "Asia/Kuala_Lumpur" >  /etc/timezone \
      && apk del tzdata \
      && rm -rf /var/cache/apk/*

ADD duply.properties /root/.duply/backupconfiguration/conf

RUN chmod 600 /root/.duply/backupconfiguration/conf
ADD crontab /var/spool/cron/crontabs/root

CMD crond -l 2 -f
## RUN rm -rf /var/cache/apk/*

# ADD crontab /etc/crontab.schedule
# ADD configureCron.sh /usr/bin/configureCron
#
# CMD configureCron && rsyslogd && cron && tail -f  /var/log/cron.log
#