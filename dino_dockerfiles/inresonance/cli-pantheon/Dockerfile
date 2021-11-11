FROM docksal/cli:1.2-php7

LABEL maintainer "Sean Dietrich <sean.dietrich@inresonance.com>"

# Install the PHP extensions we need
RUN \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" -y --force-yes --no-install-recommends install \
    php7.0-fpm \
    php7.0-dev \
    bzip2 \
    libbz2-dev \
    libc-client2007e-dev \
    libjpeg-dev \
    libkrb5-dev \
    libldap2-dev \
    libmagickwand-dev \
    libmcrypt-dev \
    libpng12-dev \
    libpq-dev \
    libxml2-dev \
    xfonts-base \
    xfonts-75dpi \
    wkhtmltopdf \
    && pecl install imagick \
    && pecl install oauth-2.0.2 \
    && pecl install redis-3.0.0 \
    && mkdir -p /srv/bin \
    && cd /srv/bin \
    && curl -fsSL "https://github.com/Medium/phantomjs/releases/download/v2.1.1/phantomjs-2.1.1-linux-x86_64.tar.bz2" | tar -xjv \
    && mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /srv/bin/phantomjs \
    && rm -rf phantomjs-2.1.1-linux-x86_64 && rm -f phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && chmod +x /srv/bin/phantomjs \
    && mkdir -p /usr/share/drush/commands && mkdir -p /root/.terminus/cache \
    && cd /usr/share/drush/commands \
    && curl -L "http://ftp.drupal.org/files/projects/registry_rebuild-7.x-2.3.tar.gz" | tar -zvx \
    && curl -O "https://raw.githubusercontent.com/drush-ops/config-extra/1.0.1/config_extra.drush.inc" \
    && DEBIAN_FRONTEND=noninteractive apt-get -y clean \
    && DEBIAN_FRONTEND=noninteractive apt-get -y autoclean \
    && DEBIAN_FRONTEND=noninteractive apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*\
    && rm -rf \
    && rm -rf /var/lib/cache/* \
    && rm -rf /var/lib/log/* \
    && rm -rf /tmp/*

RUN \
  # PHP-FPM settings
  ## /etc/php/7.0/fpm/php.ini
  sed -i '/max_execution_time =/c max_execution_time = 120' /etc/php/7.0/fpm/php.ini && \
  sed -i '/auto_prepend_file =/c auto_prepend_file = /opt/php/prepend.php' /etc/php/7.0/fpm/php.ini && \
  sed -i '/variables_order =/c variables_order = "EGPCS"' /etc/php/7.0/fpm/php.ini && \
  # PHP CLI settings
  ## /etc/php/7.0/cli/php.ini
  sed -i '/variables_order =/c variables_order = "EGPCS"' /etc/php/7.0/cli/php.ini && \
  sed -i '/auto_prepend_file =/c auto_prepend_file = /opt/php/prepend.php' /etc/php/7.0/cli/php.ini

RUN mkdir -p /opt/php
COPY config/php/prepend.php /opt/php/prepend.php
COPY startup.sh /opt/startup.sh

RUN chmod 777 /opt

USER docker

# Install Terminus
RUN composer create-project -d /opt --prefer-dist --no-dev pantheon-systems/terminus:^1
RUN cd /opt/terminus && composer update
RUN mkdir -p ~/.terminus/plugins

# Install Terminus Rsync
RUN composer create-project --no-dev -d ~/.terminus/plugins pantheon-systems/terminus-rsync-plugin:~1
RUN cd ~/.terminus/plugins/terminus-rsync-plugin && composer update

ENV PATH="/opt/terminus/bin:${PATH}" \
    FRAMEWORK=drupal8 \
    PANTHEON_SITE=docksal \
    PANTHEON_ENVIRONMENT=docksal \
    PANTHEON_BINDING=docksal \
    PANTHEON_DATABASE_HOST=db \
    PANTHEON_DATABASE_PORT=3306 \
    PANTHEON_DATABASE_USERNAME=user \
    PANTHEON_DATABASE_PASSWORD=user \
    PANTHEON_DATABASE_DATABASE=default \
    DRUPAL_HASH_SALT="some random salt"
