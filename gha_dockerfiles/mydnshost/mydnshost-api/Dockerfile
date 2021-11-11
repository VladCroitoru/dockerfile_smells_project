FROM registry.shanemcc.net/mydnshost-public/api-base AS api-base

FROM registry.shanemcc.net/mydnshost-public/api-docker-base:latest
MAINTAINER Shane Mc Cormack <dataforce@dataforce.org.uk>

COPY --from=api-base /dnsapi /dnsapi

COPY ./docker /dnsapi/docker
COPY ./templates /dnsapi/templates
COPY ./web /dnsapi/web

RUN \
  rm -Rfv /var/www/html && \
  ln -s /dnsapi/web /var/www/html && \
  mkdir /bind && \
  chown www-data: /dnsapi && \
  chown -Rfv www-data: /dnsapi/web /dnsapi/templates /var/www /bind && \
  groupadd -for -g 999 docker && \
  usermod -aG docker www-data

ENTRYPOINT ["/dnsapi/docker/run.sh"]
