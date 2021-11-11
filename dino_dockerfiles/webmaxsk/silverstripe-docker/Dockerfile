FROM nodesource/jessie:5.1.0
MAINTAINER Pali Ondras <ondras@webmax.sk>

### SET UP
ENV DEBIAN_FRONTEND=noninteractive

# BASE jessie-backports O/S with some helpful tools
RUN echo "deb http://http.debian.net/debian jessie-backports main" >> /etc/apt/sources.list
RUN apt-get -qq update && \
	apt-get -qqy install sudo wget lynx telnet nano curl make git-core locales \
	&& apt-get clean

# Local settings for local people don't touch the things! :)
RUN echo "LANG=en_GB.UTF-8\n" > /etc/default/locale && \
	echo "en_GB.UTF-8 UTF-8\n" > /etc/locale.gen && \
	locale-gen

# MARIADB
RUN apt-get -yqq install mariadb-server && \
  sed -i 's/^\(bind-address\s.*\)/# \1/' /etc/mysql/my.cnf && \
  echo "mysqld_safe &" > /tmp/config && \
  echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \
  echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" WITH GRANT OPTION;'" >> /tmp/config && \
  bash /tmp/config && \
  rm -f /tmp/config && \
  apt-get clean

# APACHE, PHP & SUPPORT TOOLS
RUN apt-get -yqq install apache2 \
	php5-cli libapache2-mod-php5 php5-mysqlnd php5-mcrypt php5-tidy php5-curl\
	php5-gd php-pear &&\
	apt-get clean

#  - Phpunit, Composer, Phing
RUN wget https://phar.phpunit.de/phpunit.phar && \
	chmod +x phpunit.phar && \
	mv phpunit.phar /usr/local/bin/phpunit && \
	wget https://getcomposer.org/composer.phar && \
	chmod +x composer.phar && \
	mv composer.phar /usr/local/bin/composer && \
	pear channel-discover pear.phing.info && \
	pear install phing/phing

# SilverStripe Apache Configuration
# RUN if [ ! -d /var/www/logs]; then mkdir /var/www/logs; fi

RUN rm /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite && \
	if [ -f /var/www/index.html]; then rm /var/www/index.html; fi

RUN echo "date.timezone = Europe/Bratislava" >> /etc/php5/apache2/php.ini

ADD startup /usr/local/bin/startup
ADD mysspak /usr/local/bin/mysspak
ADD mycomposer /usr/local/bin/mycomposer
ADD apache-default-vhost /etc/apache2/sites-available/000-default.conf
ADD _ss_environment.php /var/_ss_environment.php

# SilverStripe SSPAK installation
RUN echo "phar.readonly = Off" >> /etc/php5/cli/php.ini
RUN curl -sS https://silverstripe.github.io/sspak/install | php -- /usr/local/bin

####
## Commands and ports
EXPOSE 80

# Run apache in foreground mode
RUN chmod 755 /usr/local/bin/startup
WORKDIR /var/www

CMD ["/usr/local/bin/startup"]

ENV LANG en_GB.UTF-8
