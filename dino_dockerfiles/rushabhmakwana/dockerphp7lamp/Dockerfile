FROM ubuntu:16.04
MAINTAINER Rushabh Makwana <rushabh.makwana@multidots.com>
RUN apt-get -y update
RUN apt-get -y install git curl libcurl3 libcurl3-dev
RUN apt-get -y install apache2 
RUN apt-get install -y php7.0 libapache2-mod-php7.0 php7.0-cli php7.0-curl php7.0-common php7.0-mbstring php7.0-gd php7.0-intl php7.0-xml php7.0-mysql php-imagick php7.0-mcrypt php7.0-zip
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN apt-get -y install wget
RUN wget http://pear.php.net/go-pear.phar
RUN php go-pear.phar
RUN pear install --alldeps php_codesniffer