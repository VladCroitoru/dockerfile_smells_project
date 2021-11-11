FROM 1and1internet/ubuntu-16:unstable

MAINTAINER James Eckersall <james.eckersall@1and1.co.uk>

ENV DEBIAN_FRONTEND noninteractive

COPY files /
RUN \
  apt-get -y update && \
  apt-get -y install apt-transport-https && \
  curl https://packagecloud.io/gpg.key | apt-key add - && \
  echo "deb https://packagecloud.io/grafana/stable/debian/ wheezy main" > /etc/apt/sources.list.d/grafana.list && \
  apt-get update && \
  apt-get -o Dpkg::Options::=--force-confold -y install graphite-web graphite-carbon grafana nginx uwsgi uwsgi-plugin-python && \
  apt-get -y clean && \
  rm -rf /var/lib/apt/lists/* && \
  chmod 0755 /hooks/supervisord-pre.d/* /hooks/entrypoint-pre.d/* 2> /dev/null || true && \
  mkdir -p /usr/share/grafana/data/log /data || true && \
  chmod -R 777 /usr/share/grafana/data/log /etc/nginx/nginx.conf /etc/graphite/local_settings.py /var/log /var/lib/nginx /data && \
  chmod 644 /etc/grafana/grafana.ini && \
  sed -i -e '/import graphite.metrics.search/d' /usr/share/graphite-web/graphite.wsgi && \
  echo "daemon off;" >> /etc/nginx/nginx.conf && \
  sed -i -e '/^user www-data;/d' /etc/nginx/nginx.conf

COPY files/etc/carbon/storage-schemas.conf /etc/carbon/

EXPOSE 2003 8080
