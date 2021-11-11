FROM webdevops/php-nginx:7.2

# Add application dir
RUN mkdir -p /app/
WORKDIR /app/

# Install current Nginx
RUN echo "deb http://nginx.org/packages/debian/ stretch nginx" >> /etc/apt/sources.list \
  && echo "deb-src http://nginx.org/packages/debian/ stretch nginx" >> /etc/apt/sources.list \
  && curl http://nginx.org/keys/nginx_signing.key > /tmp/nginx_signing.key \
  && apt-key add /tmp/nginx_signing.key \
  && apt-get update \
  && export DEBIAN_FRONTEND=noninteractive \
  && apt-get install -y dirmngr \
  && mkdir ~/.gnupg && echo "disable-ipv6" >> ~/.gnupg/dirmngr.conf \ 
  && apt-get -o Dpkg::Options::="--force-overwrite" -o Dpkg::Options::="--force-confnew" install -y nginx

# Add directory for PHP socket
RUN mkdir -p /var/run/php

# Configure PHP
COPY config/php/99-docker.php.ini /usr/local/etc/php/conf.d/99-docker.ini

# Configure PHP FPM
COPY config/php/application.conf /usr/local/etc/php-fpm.d/application.conf

# Install APCu / APC backwards compatibility
RUN pecl -d preferred_state=beta install apcu_bc \
  && echo "extension=apc.so" | tee /opt/docker/etc/php/apcu-bc.ini \
  && ln -sf /opt/docker/etc/php/apcu-bc.ini /usr/local/etc/php/conf.d/apcubc.ini

# Configure Blackfire
COPY config/php/97-blackfire.php.ini /opt/docker/etc/php/blackfire.ini
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \
  && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \
  && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \
  && mv /tmp/blackfire-*.so $(php -r "echo ini_get('extension_dir');")/blackfire.so \
  && ln -sf /opt/docker/etc/php/blackfire.ini /usr/local/etc/php/conf.d/97-blackfire.ini \
  && chown root:root $(php -r "echo ini_get('extension_dir');")/blackfire.so

# Configure Nginx
COPY config/nginx/mime.types /etc/nginx/mime.types
COPY config/nginx/fastcgi_params /etc/nginx/fastcgi_params
COPY config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY config/nginx/vhost.conf /opt/docker/etc/nginx/vhost.conf
RUN rm -f /opt/docker/etc/nginx/vhost.common.d/*
COPY config/nginx/vhost.common.d /opt/docker/etc/nginx/vhost.common.d

# Configure cronjob
COPY config/cron/crontab /etc/cron.d/typo3
COPY config/cron/cron.conf /opt/docker/etc/supervisor.d/cron.conf

# Configure local SSH server
RUN apt-get --yes install openssh-server sudo \
  && mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config \
  && sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
  && touch /root/.Xauthority \
  && true

ADD config/sshd/authorized_keys /tmp/authorized_keys

RUN \
  for MYHOME in /root /home/docker; do \
    mkdir -p ${MYHOME}/.ssh; \
    chmod go-rwx ${MYHOME}/.ssh; \
    cp /tmp/authorized_keys ${MYHOME}/.ssh/authorized_keys; \
    chmod go-rw ${MYHOME}/.ssh/authorized_keys; \
  done \
  && useradd docker \
    && passwd -d docker \
    && mkdir -p /home/docker \
    && chown docker:docker /home/docker \
    && addgroup docker staff \
    && addgroup docker sudo \
    && true \
  && chown -R docker:docker /home/docker/.ssh;

# Install MySQL client
RUN echo "deb http://repo.mysql.com/apt/debian stretch mysql-5.7" >> /etc/apt/sources.list \
  && gpg --recv-keys 5072E1F5 || true \
  && sleep 1s \
  && gpg --recv-keys 5072E1F5 \
  && gpg --export 5072E1F5 > /etc/apt/trusted.gpg.d/5072E1F5.gpg \
  && apt-get update \
  && apt-get --yes install mysql-client

# Clean up image
RUN docker-image-cleanup

# Add utilities to container
COPY util /usr/local/bin/rmutil
RUN chmod a+x /usr/local/bin/rmutil/*

# Add user and fix permissions
RUN adduser www-data application
RUN chmod 0644 /etc/cron.d/typo3
