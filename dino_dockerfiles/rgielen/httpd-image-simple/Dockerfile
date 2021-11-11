FROM ubuntu:18.04
MAINTAINER "Rene Gielen" <rgielen@apache.org>

RUN apt-get update && apt-get upgrade -y \
      && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
           apache2 \
           curl \
           ca-certificates \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/* \
      && rm -rf /tmp/*

COPY httpd-foreground /usr/local/bin/

EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
