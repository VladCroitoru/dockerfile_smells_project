FROM ubuntu:16.04

LABEL maintainer.name="Igor Bronovskyi" maintainer.email="admin@brun.if.ua"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --force-yes software-properties-common \
    && apt-add-repository ppa:nginx/development -y \
    && apt-add-repository ppa:chris-lea/redis-server -y \
    && LC_ALL=C.UTF-8 apt-add-repository ppa:ondrej/apache2 -y \
    && LC_ALL=C.UTF-8 apt-add-repository ppa:ondrej/php -y \
    && apt-get update \
    && apt-get install -y --force-yes build-essential curl gcc git libmcrypt4 libpcre3-dev \
        make python2.7 python-pip sendmail supervisor unattended-upgrades unzip whois redis-server \
        ruby-dev libsqlite3-dev libxrender1 dbus-user-session \
    && apt-get install -y --force-yes php7.1-cli php7.1-dev \
        php7.1-pgsql php7.1-sqlite3 php7.1-gd \
        php7.1-curl php7.1-memcached \
        php7.1-imap php7.1-mysql php7.1-mbstring \
        php7.1-xml php7.1-imagick php7.1-zip php7.1-bcmath php7.1-soap \
        php7.1-intl php7.1-readline php7.1-mcrypt php7.1-fpm \
    && apt-get install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 \
        libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 \
        libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 \
        libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 \
        ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils \
    && apt-get install -y dnsmasq jq vim nano \
    && curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer \
    && curl --silent --location https://deb.nodesource.com/setup_10.x | bash - \
    && gem install mailcatcher \
    && apt-get update && apt-get install -y --force-yes nodejs \
    && echo "mysql-server mysql-server/root_password password root" | debconf-set-selections \
    && echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections \
    && apt-get install -y mysql-server \
    && sed -i '/^bind-address/s/bind-address.*=.*/bind-address = */' /etc/mysql/mysql.conf.d/mysqld.cnf \
    && service mysql start \
    && apt-get install wget gnupg2 openjdk-8-jdk -y \
    && wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - \
    && wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.7.2.deb && dpkg -i elasticsearch-6.7.2.deb \
    && update-rc.d elasticsearch defaults 95 10 \
    && mysql -uroot -proot -e "GRANT ALL ON *.* TO root@'%' IDENTIFIED BY 'root';" \
    && sed -i '/^bind/s/bind.*/bind 0.0.0.0/' /etc/redis/redis.conf \
    && apt-get autoclean && apt-get clean && apt-get autoremove \
    && rm -rf /root/.npm /root/.composer /tmp/* /var/lib/apt/lists/*

# Configuration
RUN sed -i "s/;opcache.enable=1/opcache.enable=1/" /etc/php/7.1/cli/php.ini \
	&& sed -i "s/;opcache.enable_cli=0/opcache.enable_cli=1/" /etc/php/7.1/cli/php.ini \
	&& sed -i "s/;opcache.memory_consumption=128/opcache.memory_consumption=512/" /etc/php/7.1/cli/php.ini \
	&& sed -i "s/;opcache.interned_strings_buffer=8/opcache.interned_strings_buffer=32/" /etc/php/7.1/cli/php.ini \
	&& sed -i "s/;opcache.max_accelerated_files=10000/opcache.max_accelerated_files=32531/" /etc/php/7.1/cli/php.ini \
	&& sed -i "s/;opcache.validate_timestamps=1/opcache.validate_timestamps=1/" /etc/php/7.1/cli/php.ini \
	&& sed -i "s/;opcache.save_comments=1/opcache.save_comments=1/" /etc/php/7.1/cli/php.ini \
	&& sed -i "s/;opcache.fast_shutdown=0/opcache.fast_shutdown=0/" /etc/php/7.1/cli/php.ini
RUN curl -o /usr/local/bin/minio https://dl.minio.io/server/minio/release/linux-amd64/minio \ 
	&& chmod +x /usr/local/bin/minio \
	&& curl -o /usr/local/bin/minio-client https://dl.minio.io/client/mc/release/linux-amd64/mc \
	&& chmod +x /usr/local/bin/minio-client \
    && curl -L -o /usr/local/bin/slack https://git.io/fAhXh \
    && chmod +x /usr/local/bin/slack

RUN composer global require hirak/prestissimo

ADD ./minio /etc/init.d/minio
ADD ./pipeline.sh /pipeline.sh
ADD ./pipeline-testdox.sh /pipeline-testdox.sh
ADD ./pipeline-on-failure.sh /pipeline-on-failure.sh
ADD ./clone /usr/bin/clone
ADD ./pipeline-parallel.sh /pipeline-parallel.sh

WORKDIR /var/www/html/
