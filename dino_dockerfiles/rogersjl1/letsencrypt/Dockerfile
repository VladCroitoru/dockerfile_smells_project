FROM debian:jessie-backports

RUN apt-get update \
  && apt-get install -y letsencrypt -t jessie-backports \
  && apt-get install -y --no-install-recommends cron \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p /etc/letsencrypt \
  && mkdir -p /var/www/letsencrypt

VOLUME ["/var/www/letsencrypt", "/etc/letsencrypt"]
