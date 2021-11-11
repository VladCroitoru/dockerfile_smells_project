FROM debian:stretch
MAINTAINER Dylan Sweetensen <dylan@sweetdigital.nz>

# SET UP
RUN apt-get -qq update

RUN apt-get -qqy install sudo wget lynx telnet nano curl make git-core locales bzip2 

RUN echo "LANG=en_US.UTF-8\n" > /etc/default/locale && \
	echo "en_US.UTF-8 UTF-8\n" > /etc/locale.gen && \
	locale-gen

# KNOWN HOSTS
ADD known_hosts /root/.ssh/known_hosts

RUN echo "deb http://packages.dotdeb.org stretch all" >> /etc/apt/sources.list.d/dotdeb.org.list && \
    echo "deb-src http://packages.dotdeb.org stretch all" >> /etc/apt/sources.list.d/dotdeb.org.list && \
    wget -O- http://www.dotdeb.org/dotdeb.gpg | apt-key add -


# APACHE, MYSQL, PHP & SUPPORT TOOLS
RUN apt-get -y install apt-transport-https lsb-release ca-certificates
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/php.list

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get -qqy install apache2 \
    mysql-client \
    php7.1 \
    php7.1-cli \
    libapache2-mod-php7.1 \
    php7.1-gd \
    php7.1-json \
    php7.1-ldap \
    php7.1-mbstring \
    php7.1-mysql \
    php7.1-pgsql \
    php7.1-sqlite3 \
    php7.1-xml \
    php7.1-xsl \
    php7.1-zip \
    php7.1-soap \
    php7.1-fpm \
    php7.1-curl \
    php7.1-cli \
    php7.1-dev \
    php7.1-intl \
    php-pear \
    libsasl2-dev \
    sendmail

#  Phpunit, Composer, Phing, SSPak
RUN wget https://phar.phpunit.de/phpunit-3.7.37.phar && \
	chmod +x phpunit-3.7.37.phar && \
	mv phpunit-3.7.37.phar /usr/local/bin/phpunit && \
	wget https://getcomposer.org/composer.phar && \
	chmod +x composer.phar && \
	mv composer.phar /usr/local/bin/composer

# SilverStripe Apache Configuration
RUN a2enmod rewrite && \
	rm -r /var/www/html && \
    echo "date.timezone = Pacific/Auckland" >> /etc/php/7.1/apache2/php.ini

ADD apache-foreground /usr/local/bin/apache-foreground
ADD apache-default-vhost /etc/apache2/sites-available/000-default.conf

## These are not specifically SilverStripe related and could be removed on a more optimised image

# NodeJS and common global NPM modules

# Update to node 8
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs

# Install yarn
RUN npm install -g yarn

# LetsEncrypt 
RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' | sudo tee /etc/apt/sources.list.d/backports.list
RUN apt-get update
RUN apt-get -qqy install python-certbot-apache -t jessie-backports

# SilverStripe Upgrader
RUN composer global require silverstripe/upgrader && \
    echo 'export PATH=$PATH:/root/.composer/vendor/bin/' >> /root/.bash_profile

####
## Commands and ports
EXPOSE 80

VOLUME /var/www

# Run apache in foreground mode, because Docker needs a foreground
WORKDIR /var/www
CMD ["/usr/local/bin/apache-foreground"]

ENV LANG en_US.UTF-8
