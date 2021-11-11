FROM quay.io/letsencrypt/letsencrypt

ADD crontab /etc/crontab
ADD start-cron.sh /usr/bin/start-cron.sh
ADD renew‑letsencrypt.sh /usr/bin/renew‑letsencrypt.sh

RUN chmod +x /usr/bin/start-cron.sh
RUN touch /var/log/cron.log
RUN mkdir -p /var/log/letsencrypt
RUN apt-get update && apt-get install -y git docker.io rsyslog

VOLUME /var/run/docker.sock /etc/letsencrypt 

ENTRYPOINT [ "/usr/bin/start-cron.sh" ]