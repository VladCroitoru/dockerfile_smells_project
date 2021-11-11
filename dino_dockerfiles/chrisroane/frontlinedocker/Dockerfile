# Set the base image
FROM ubuntu:16.04
MAINTAINER Chris Roane <chris.roane@fourkitchens.com>

# This was started from the docker file here:
# https://hub.docker.com/r/fauria/lamp/~/dockerfile/

RUN DEBIAN_FRONTEND=noninteractive
# Replace shell with bash so we can source files.
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y \
	php7.0 \
	php7.0-bz2 \
	php7.0-cgi \
	php7.0-cli \
	php7.0-common \
	php7.0-curl \
	php7.0-dev \
	php7.0-enchant \
	php7.0-fpm \
	php7.0-gd \
	php7.0-gmp \
	php7.0-imap \
	php7.0-interbase \
	php7.0-intl \
	php7.0-json \
	php7.0-ldap \
	php7.0-mcrypt \
	php7.0-mysql \
	php7.0-odbc \
	php7.0-opcache \
	php7.0-pgsql \
	php7.0-phpdbg \
	php7.0-pspell \
	php7.0-readline \
	php7.0-recode \
	php7.0-snmp \
	php7.0-sqlite3 \
	php7.0-sybase \
	php7.0-tidy \
	php7.0-xmlrpc \
	php7.0-xsl \
	unzip \
	wget \
	sudo \
	ruby-sass \
	snmp \
	iputils-ping

RUN apt-get install apache2 libapache2-mod-php7.0 -y
RUN apt-get install git composer nano tree vim curl ftp php7.0-mbstring default-jre -y
RUN apt-get install -y openjdk-8-jre-headless xvfb libxi6 libgconf-2-4
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --yes --force-yes --install-recommends linux-generic-hwe-16.04

# Install MariaDB
RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0xcbcb082a1bb943db && \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - && \
  echo "deb [arch=amd64,i386,ppc64el] http://mirror.lstn.net/mariadb/repo/10.2/ubuntu xenial main" > /etc/apt/sources.list.d/mariadb.list && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated mariadb-server && \
  rm -rf /var/lib/apt/lists/* && \
  sed -i 's/^\(bind-address\s.*\)/# \1/' /etc/mysql/my.cnf && \
  echo "mysqld_safe &" > /tmp/config && \
  echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \
  bash /tmp/config && \
  rm -f /tmp/config && \
  apt-get clean all

# Install Chrome 55 + dependencies
RUN apt-get update
RUN apt-get install -y libnss3-1d libxss1 libgconf2-4 libappindicator1 libindicator7 libpango1.0-0 fonts-liberation xdg-utils
RUN wget http://bbgentoo.ilb.ru/distfiles/google-chrome-stable_55.0.2883.87-1_amd64.deb
RUN sudo dpkg -i google-chrome-stable_55.0.2883.87-1_amd64.deb
RUN sudo apt-get -f install

# Install Chromedriver 2.24
RUN wget --no-check-certificate https://chromedriver.storage.googleapis.com/2.24/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN sudo mv -f chromedriver /usr/local/bin/chromedriver
RUN sudo chown -R root:root /usr/local/bin/chromedriver
RUN sudo chmod -R 0755 /usr/local/bin/chromedriver

ENV LOG_STDOUT **Boolean**
ENV LOG_STDERR **Boolean**
ENV LOG_LEVEL warn
ENV ALLOW_OVERRIDE All
ENV DATE_TIMEZONE UTC
ENV TERM dumb

VOLUME /var/www/html
VOLUME /var/log/httpd
VOLUME /var/log/mysql
VOLUME ["/etc/mysql", "/var/lib/mysql"]

# Node
RUN mkdir -p /tmp/node
WORKDIR /tmp/node
ENV NODE_VERSION 6.1.0
ENV NPM_VERSION 5.4.0
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.gz" \
  && npm install -g npm@"$NPM_VERSION" \
  && npm cache clear --force \
  && rm -rf /tmp/*
RUN sudo npm install -g gulp

# Install Drush
RUN sudo composer global require drush/drush:8.1.2
ENV PATH="/root/.composer/vendor/bin:${PATH}"

# Set some git config.
RUN git config --global core.fileMode false
RUN git config --global http.sslverify false

# Disable host checking.
RUN mkdir $HOME/.ssh/ && echo "StrictHostKeyChecking no" >> "$HOME/.ssh/config"

# Install Solr.
WORKDIR "~/"
RUN wget http://archive.apache.org/dist/lucene/solr/4.7.2/solr-4.7.2.tgz \
  && tar -xvzf solr-4.7.2.tgz
RUN curl https://ftp.drupal.org/files/projects/apachesolr-7.x-1.x-dev.tar.gz | tar -xz
RUN cp -r apachesolr/solr-conf/solr-4.x/* solr-4.7.2/example/solr/collection1/conf
RUN mv solr-4.7.2 ~/solr
RUN rm -rf apachesolr solr-4.7.2.tgz apachesolr-7.x-1.x-dev.tar.gz

# Download Selenium
RUN wget -O ~/selenium-server-standalone-3.3.1.jar http://selenium-release.storage.googleapis.com/3.3/selenium-server-standalone-3.3.1.jar

# Setup apache
RUN sudo mkdir /root/medstat
RUN sudo mkdir /root/medstat/build
COPY ./config/default-apache-page.html /root/medstat/build/
RUN sudo mv /root/medstat/build/default-apache-page.html /root/medstat/build/index.html
RUN sudo chown -R www-data:www-data /root/medstat/build
RUN sudo chmod -R g+rwX /root/medstat/build
COPY ./config/medstat.conf /etc/apache2/sites-available/
RUN sudo a2ensite medstat
RUN sudo a2enmod rewrite

# If we don't do this apach can't access the site files.
RUN chmod +rx /root

CMD ["supervisord", "--nodaemon"]
CMD ["service", "php7-fpm", "start"]
CMD ["service", "apache2", "start"]
CMD ["mysqld_safe"]

# Remove the medstat directory so circleci doesn't fail.
RUN rm -R /root/medstat

EXPOSE 8080
EXPOSE 3306
