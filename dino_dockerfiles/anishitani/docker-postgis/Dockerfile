FROM anishitani/docker-postgresql

MAINTAINER André Nishitani <andre.nishitani@gmail.com>

ENV PGIS_VERSION 2.1

RUN /scripts/init_squid_cache.sh

USER root

RUN apt-get install -y postgresql-$PG_VERSION-postgis-$PGIS_VERSION \
  && apt-get autoclean && apt-get --purge -y autoremove \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN /scripts/stop_squid_cache.sh

USER postgres

# Set the default command to run when starting the container
CMD ["/scripts/start.sh"]
