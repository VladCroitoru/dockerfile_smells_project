FROM php:7.1-cli
MAINTAINER Shane Mc Cormack <dataforce@dataforce.org.uk>

COPY . /socketRelayServer

WORKDIR /socketRelayServer

RUN \
  apt-get update && apt-get install -y git unzip && \
  docker-php-source extract && \
  docker-php-ext-install pcntl && \
  docker-php-source delete && \
  useradd socketrelayserver && \
  mkdir -p /home/socketrelayserver/ && \
  chown -Rfv socketrelayserver: /socketRelayServer /home/socketrelayserver && \
  curl -sS https://getcomposer.org/installer | php -- --no-ansi --install-dir=/usr/bin --filename=composer && \
  su socketrelayserver --shell=/bin/bash -c "cd /socketRelayServer; /usr/bin/composer install" && \
  chmod a+x /socketRelayServer/run.php

EXPOSE 3302

VOLUME ["/data"]

ENV FAILFILE /data/.failedMessages
ENV LOCALCONF /data/config.local.php

CMD ["/socketRelayServer/run.php"]
