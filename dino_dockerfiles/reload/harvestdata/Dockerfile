FROM phusion/baseimage:0.9.17

COPY docker/etc/ /etc/

COPY ./ /harvestdata/

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      php5-cli \
      php5-curl \
      apache2 \
  && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Overwrite index with Rasmus' .
COPY docker/index.html /var/www/html/index.html

# Link output into /var/www/html.
RUN \
  ln -s /harvestdata/data/billableYesterday.xml /var/www/html/billableyesterday.xml && \
  ln -s /harvestdata/data/ /var/www/html/data && \
  ln -s /harvestdata/data/today.xml /var/www/html/today.xml && \
  crontab /harvestdata/docker/crontab

ENV HARVESTDATA_ACCOUNT ""
ENV HARVESTDATA_USERNAME ""
ENV HARVESTDATA_PASSWORD ""

EXPOSE 80
