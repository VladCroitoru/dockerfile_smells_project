FROM php:5.5-apache

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    openssh-server \
    supervisor \
    git-core \
    libmcrypt-dev \
    zlib1g-dev \
  && docker-php-ext-install -j$(nproc) mcrypt \
  && docker-php-ext-install -j$(nproc) zip \
  && docker-php-ext-install -j$(nproc) mbstring \
  && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

RUN apt-get update && apt-get install -y nodejs

RUN curl -sSL https://getcomposer.org/installer | php \
  && mv composer.phar /usr/local/bin/composer

# supervisord
ADD config/supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD config/supervisord/apache2.conf /etc/supervisor/conf.d/apache2.conf
ADD config/supervisord/sshd.conf /etc/supervisor/conf.d/sshd.conf
# apache2
ADD config/apache/default.conf /etc/apache2/sites-available/000-default.conf

RUN a2enmod rewrite

RUN usermod -u 1000 www-data

EXPOSE 22 80 9001
CMD ["/usr/bin/supervisord"]