FROM nginx:latest

VOLUME ["/etc/nginx/conf.d", "/var/log/nginx"]

ADD res/* /
ADD nginx/ /etc/nginx/

RUN chmod +x /*.sh \
    && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
    && apt-get update \
    && apt-get install -y nano wget vim \
    && wget https://dl.eff.org/certbot-auto \
    && chmod a+x certbot-auto \
    && mv certbot-auto /usr/bin/certbot \
    && rm -fv /var/log/nginx/* \
    && touch /var/log/access.log /var/log/error.log \
    && mkdir -v /etc/nginx/ssl \
    && openssl dhparam -out /etc/nginx/ssl/dhparam.pem 512 \
    && echo "/usr/bin/letsencrypt renew >> /var/log/nginx/le-renew.log; /bin/systemctl reload nginx" >/etc/cron.daily/certbot-renew \
    && chmod +x /etc/cron.daily/certbot-renew
#    && certbot-auto -n \
#   nginx -t \

EXPOSE 80
EXPOSE 443

CMD /entrypoint.sh