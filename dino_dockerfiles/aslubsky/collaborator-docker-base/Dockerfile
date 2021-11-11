FROM debian:9.4-slim

RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y \
    wget \
    curl \
    dialog \
    bsdutils \
    make \
    g++ \
    gnupg \
    cron \
    unzip \
    git \
    supervisor \
    catdoc \
    certbot \
    nano \
    poppler-utils \
    libav-tools \
    ca-certificates \
    apt-transport-https \
    gpac

RUN cd /tmp && wget https://github.com/htacg/tidy-html5/releases/download/5.4.0/tidy-5.4.0-64bit.deb && dpkg -i tidy-5.4.0-64bit.deb

RUN echo "deb http://nginx.org/packages/debian/ stretch nginx" > /etc/apt/sources.list.d/nginx.list
RUN echo "deb-src http://nginx.org/packages/debian/ stretch nginx" >> /etc/apt/sources.list.d/nginx.list
RUN cd /tmp && wget http://nginx.org/keys/nginx_signing.key && apt-key add nginx_signing.key

RUN wget -q https://packages.sury.org/php/apt.gpg -O- | apt-key add -
RUN echo "deb https://packages.sury.org/php/ stretch main" | tee /etc/apt/sources.list.d/php.list

RUN apt-get update

RUN apt-get install -y nginx logrotate php7.1-cli php7.1-mysql php7.1-xml php7.1-curl php7.1-gd php7.1-mcrypt php7.1-intl php7.1-zip php7.1-mbstring php7.1-fpm php7.1-sqlite php7.1-ldap php7.1-redis

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
RUN /usr/bin/composer.phar self-update

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

RUN npm install -g bower node-gyp gulp

#
# Remove the packages that are no longer required after the package has been installed
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -q -y
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean -y -q
RUN DEBIAN_FRONTEND=noninteractive apt-get clean -y

# Remove all non-required information from the system to have the smallest
# image size as possible
# ftp://cgm_gebraucht%40used-forklifts.org:bZAo6dH1cyxhJpgJwO@ftp.strato.com/
RUN rm -rf /usr/share/doc/* /usr/share/man/?? /usr/share/man/??_* /usr/share/locale/* /var/cache/debconf/*-old /var/lib/apt/lists/* /tmp/*

