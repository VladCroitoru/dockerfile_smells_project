FROM jenkins:latest

MAINTAINER Michael Chelen <michael.chelen@gmail.com>


USER root

RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 14AA40EC0831756756D7F66C4F4EA0AAE5267A6C; \
  echo "deb http://ppa.launchpad.net/ondrej/php5-5.6/ubuntu trusty main" >> /etc/apt/sources.list; \
  echo "deb-src http://ppa.launchpad.net/ondrej/php5-5.6/ubuntu trusty main" >> /etc/apt/sources.list


RUN apt-get update;

RUN export DEBIAN_FRONTEND=noninteractive; \
  apt-get update; \
  apt-get -qq install php5 php5-cli php5-xsl php5-json php5-curl php5-sqlite php5-mysqlnd php5-xdebug php5-intl php5-mcrypt php-pear curl git ant

RUN ln -s /var/jenkins_home/composer /usr/local/bin/

USER jenkins

RUN bash -c 'curl -sS https://getcomposer.org/installer | php -- --install-dir=/var/jenkins_home --filename=composer'






