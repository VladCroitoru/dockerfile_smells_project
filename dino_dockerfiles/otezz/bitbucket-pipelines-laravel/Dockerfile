FROM ubuntu:xenial

MAINTAINER Seto Kuslaksono <kuslaksono@gmail.com>

ADD setup-mariadb.sh /setup-mariadb.sh

ENV MARIADB_VERSION 10.1
ENV MYSQL_ROOT_PASSWORD root

# Update, Fix Language and install Build Essesntial
RUN \
 apt-get update && apt-get -y upgrade &&\
 apt-get install -y --no-install-recommends locales build-essential apt-utils &&\
 echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen &&\
 locale-gen en_US.UTF-8 &&\
 /usr/sbin/update-locale LANG=en_US.UTF-8

# Install mariadb
RUN ["/bin/bash", "-c", "bash /setup-mariadb.sh"]

# Install PHP
RUN \
  LC_ALL=C.UTF-8 add-apt-repository -y -u ppa:ondrej/php && \
  apt-get update && \
  apt-get install -y git zip && \
  apt-get install -y php7.1 php7.1-cli php7.1-common php7.1-curl php7.1-dev php7.1-fpm php7.1-json php7.1-mbstring php7.1-mcrypt \
    php7.1-mysql php7.1-opcache php7.1-readline php7.1-sqlite3 php7.1-xml php7.1-zip php7.1-intl php7.1-gd php-mongodb php-xdebug && \
  apt-get autoclean && apt-get clean && apt-get autoremove

# Install Laravel Dusk support
RUN \
  apt-get update && \
  apt-get install -y chromium-browser libxpm4 libxrender1 libgtk2.0-0 libnss3 \
    libnss3-dev libxi6 libgconf-2-4 xvfb gtk2-engines-pixbuf \
    xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable \
    imagemagick x11-apps && \
  apt-get autoclean && apt-get clean && apt-get autoremove

# Install composer
RUN apt-get update && apt-get install -y curl && \
    curl -sS https://getcomposer.org/installer | php -- --filename=composer --install-dir=/usr/local/bin

# Install PHPUnit
RUN apt-get update && apt-get install -y curl && \
    curl https://phar.phpunit.de/phpunit.phar > phpunit.phar && chmod +x phpunit.phar && mv phpunit.phar /usr/local/bin/phpunit

# Install NodeJS
RUN apt-get update && apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs

# Install yarn
RUN apt-get update && apt-get install -y curl apt-transport-https && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -y yarn

# Clean up
RUN \
 apt-get autoclean && apt-get clean && apt-get autoremove
