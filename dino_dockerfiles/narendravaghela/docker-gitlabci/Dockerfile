FROM ubuntu:14.04
MAINTAINER Narendra Vaghela <narendravaghela4389@gmail.com>
RUN apt-get -y update
RUN apt-get -y install git curl libcurl3 libcurl3-dev
RUN apt-get -y install apache2 libapache2-mod-php5
RUN apt-get -y install php5 php5-cli php5-curl php5-gd php5-mysql php5-imagick php5-intl php5-mcrypt
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN apt-get -y install build-essential nodejs npm
RUN npm install -g bower
