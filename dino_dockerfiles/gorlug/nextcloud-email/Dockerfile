FROM gorlug/nextcloud:11.0.2
MAINTAINER Achim Rohn <achim@rohn.eu>

RUN apt-get update && apt-get install -y \
  libc-client2007e-dev \
  libkrb5-dev \
  mysql-client \
  && rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
  && docker-php-ext-install imap
RUN usermod -s /bin/bash www-data && sed -i 's/pm.max_children = 5/pm.max_children = 100/' /usr/local/etc/php-fpm.d/www.conf

COPY docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
