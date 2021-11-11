FROM ubuntu:trusty

RUN apt-get update && apt-get install -y cron nginx nginx-extras apache2-utils

VOLUME /media
EXPOSE 80
COPY webdav.conf /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/sites-enabled/*

COPY crontab /var/spool/cron/crontabs/root

COPY entrypoint.sh /
RUN chmod +x entrypoint.sh
CMD /entrypoint.sh && cron && nginx -g "daemon off;"
