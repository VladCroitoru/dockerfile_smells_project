FROM victorcano/ubuntu

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install php5-dev php5-mcrypt php5-curl php5-pgsql php5-mysql php5-sqlite -y
RUN apt-get install php5-memcached php5-xdebug php-apc php5-imagick php5-gd php5-geoip gcc git libpcre3-dev php-pear -y
RUN apt-get install php5-fpm nginx -y
RUN pecl install mongo -y

RUN git clone --depth=1 http://github.com/phalcon/cphalcon.git -b 1.2.3 cphalcon
RUN cd cphalcon/build && ./install;


RUN echo 'extension=phalcon.so' > /etc/php5/fpm/conf.d/phalcon.ini
RUN echo 'extension=mongo.so' > /etc/php5/fpm/conf.d/mongo.ini

ADD nginx.conf /etc/nginx/nginx.conf
ADD default /etc/nginx/sites-available/default

RUN mkdir /var/www

EXPOSE 80

CMD service php5-fpm start && nginx
