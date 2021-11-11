FROM		technopreneural/docker-ubuntu-14.04-apache2
MAINTAINER	technopreneural@yahoo.com

# Install PHP5 components
RUN		apt-get update \
		&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
			curl \
			git \
			libapache2-mod-php5 \
			php5 \
			php5-cli \
			php5-curl \
			php5-dev \
			php5-gd \
			php5-imagick \
			php5-intl \
			php5-mcrypt \
			php5-memcache \
			php5-mhash \
			php5-mysql \
			php5-pgsql \
			php5-sqlite \
			php5-xmlrpc \
			php5-xsl \

# Configure MCrypt
		&& php5enmod mcrypt \

# Install Composer
		&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
		&& php -r "if (hash_file('SHA384', 'composer-setup.php') === '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
		&& php composer-setup.php \
		&& php -r "unlink('composer-setup.php');" \
		&& mv composer.phar /usr/local/bin/composer
