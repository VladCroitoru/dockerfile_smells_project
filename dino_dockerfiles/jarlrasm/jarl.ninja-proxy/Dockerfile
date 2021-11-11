FROM nginx:latest


RUN echo 'deb http://ftp.debian.org/debian jessie-backports main'>>/etc/apt/sources.list && \
    apt-get update && \
    apt-get --yes install cron && \
    apt-get --yes install certbot -t jessie-backports && \
    rm -rf /var/lib/apt/* && \
    openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048

COPY conf.d /etc/nginx/conf.d
COPY run.sh /bin/run.sh
COPY certbot.cron /etc/cron.d/certbot

CMD ["/bin/run.sh"]
