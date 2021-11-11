FROM ubuntu:trusty
MAINTAINER Kaito Udagawa <umireon@gmail.com>

# basic setup
RUN apt-get -y update; apt-get -y upgrade; apt-get -y install software-properties-common wget; apt-get -y clean; rm -rf /var/lib/apt/lists/*

# install salt-minion
RUN add-apt-repository ppa:saltstack/salt; apt-get -y update; apt-get -y install salt-minion; apt-get -y clean; rm -rf /var/lib/apt/lists/*

# install owncloud dependencies
RUN apt-get -y update; apt-get -y install apache2 libapache2-mod-php5 php5-gd php5-curl php5-pgsql; apt-get -y clean; rm -rf /var/lib/apt/lists/*

# install owncloud distribution
RUN wget -q -O - https://download.owncloud.org/community/owncloud-7.0.2.tar.bz2 | tar xjvf - -C /var/www/html

# setup application
RUN mkdir /var/www/html/owncloud/data
RUN chown www-data:www-data /var/www/html/owncloud/data

COPY 000-default.conf /etc/apache2/sites-available/

COPY run.sh /
RUN chmod 0755 /run.sh

# image setting
VOLUME /var/www/html/owncloud/config
CMD /run.sh
EXPOSE 80

