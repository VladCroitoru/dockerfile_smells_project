FROM composer/composer

RUN mkdir -p /src/app && cd /src/app && git clone https://github.com/erikdubbelboer/phpRedisAdmin.git .
WORKDIR /src/app

RUN \
  composer install && \
  cp includes/config.environment.inc.php includes/config.inc.php

EXPOSE 80

ENTRYPOINT [ "php", "-S", "0.0.0.0:80" ]
