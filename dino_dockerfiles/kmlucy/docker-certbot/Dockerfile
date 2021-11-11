FROM debian:testing

RUN apt-get update \
  && apt-get install -y certbot \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/

CMD certbot renew

VOLUME /etc/letsencrypt
VOLUME /html
