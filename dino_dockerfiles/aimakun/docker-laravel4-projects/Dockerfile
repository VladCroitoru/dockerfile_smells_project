FROM parana/trusty-php

COPY docker-vhosts.conf /etc/apache2/sites-enabled/000-default.conf

# Set timezone
RUN echo 'date.timezone = Asia/Bangkok' > /etc/php5/apache2/php.ini

# Required extensions for this project
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        software-properties-common wget php5-mcrypt php-soap php5-intl \
        libcurl3 php5-curl gettext \
        xvfb libxrender1 \
        && php5enmod mcrypt \
        && php5enmod soap \
        && a2enmod headers

# Install wkhtmltopdf
RUN wget http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz \
		&& tar xf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz \
		&& cp wkhtmltox/bin/wkhtmltopdf /usr/bin \
		&& cp wkhtmltox/bin/wkhtmltoimage /usr/bin \
		&& rm wkhtmltox-0.12.3_linux-generic-amd64.tar.xz \
		&& rm -r wkhtmltox

# Install PHP CodeSniffer
RUN pear install PHP_CodeSniffer

# Setup locale & timezone
RUN locale-gen sv_SE.UTF-8
RUN locale-gen en_US.UTF-8

# Install PHPUnit 4.8 for PHP 5.5
RUN wget https://phar.phpunit.de/phpunit-old.phar
RUN chmod +x phpunit-old.phar
RUN mv phpunit-old.phar /usr/local/bin/phpunit

# Set default volume for image
# This would be overrided by docker-compose for updatable source code between development
COPY . /data
WORKDIR /data

# Fixes user permissions for Mac OS [https://github.com/boot2docker/boot2docker/issues/581]
RUN usermod -u 1000 www-data
RUN usermod -G staff www-data

RUN apache2 -D FOREGROUND &