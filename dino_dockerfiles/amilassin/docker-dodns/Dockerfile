FROM node:9.4.0-alpine
MAINTAINER amilassin

VOLUME "/config"


# add local files
RUN mkdir -p /etc/my_init.d

ADD startup.sh /root/startup.sh
RUN chmod +x /root/startup.sh

ADD dodns.js /root/dodns.js
ADD dodns.conf.js.default /root/dodns.conf.js.default

ADD dodns_periodic.sh /etc/periodic/15min/dodns
RUN chmod +x /etc/periodic/15min/dodns

# run cron in frontend mode, otherwise nothing will run and the container will exit right away
CMD ["/root/startup.sh"]