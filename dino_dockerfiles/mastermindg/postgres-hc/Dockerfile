FROM postgres:9.6.2-alpine
MAINTAINER Ken Jenney

COPY docker-healthcheck /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-healthcheck

HEALTHCHECK CMD ["docker-healthcheck"]
