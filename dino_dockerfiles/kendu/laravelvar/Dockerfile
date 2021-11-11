FROM debian:latest
MAINTAINER DevOps <devops@kendu.si>

RUN for dir in app framework logs storage meta views upload ; do \
      mkdir -p /var/app/${dir} ; \
    done ; \
    for dir in cache sessions views ; do \
      mkdir -p /var/app/framework/${dir} ; \
    done ; \
    chown -R www-data /var/app; \
    mkdir -p -m 777 /opt/web/bootstrap/cache; \
    chown www-data /opt/web/bootstrap/cache


VOLUME ["/var/app", "/opt/web/bootstrap/cache"]
