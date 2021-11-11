FROM certbot/certbot
LABEL maintainer="Leif Gensert <leif@leif.io>"

ENTRYPOINT ["crond", "-f"]

RUN mkdir /scripts
ADD scripts/* /scripts/

RUN echo '0 0 * * * /scripts/renew_certificates.sh > /proc/1/fd/1 2>&1' > /var/spool/cron/crontabs/root
RUN echo "" >> /var/spool/cron/crontabs/root
RUN crontab /var/spool/cron/crontabs/root
