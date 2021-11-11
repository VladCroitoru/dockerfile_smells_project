# Dockerfile for building Debian packages using current stable repo.
FROM debian:stable
MAINTAINER Ruslan Kabalin <r.kabalin@lancaster.ac.uk>

COPY sources-list /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends \
  devscripts \
  equivs \
  rsync \
  locales \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

VOLUME /package

COPY packagebuild /usr/local/bin/
COPY devscripts /root/.devscripts

RUN chmod 755 /usr/local/bin/packagebuild
ENTRYPOINT ["packagebuild"]
