FROM ubuntu:14.04

MAINTAINER Tim Sutton <tim@kartoza.com>

RUN export DEBIAN_FRONTEND=noninteractive
ENV DEBIAN_FRONTEND noninteractive
RUN dpkg-divert --local --rename --add /sbin/initctl

# Use local cached debs from host (saves your bandwidth!)
# Change ip below to that of your apt-cacher-ng host
# Or comment this line out if you do not wish to use caching
ADD 71-apt-cacher-ng /etc/apt/apt.conf.d/71-apt-cacher-ng

RUN apt-get -y update && apt-get install -y apache2 php5 php5-gd php5-pgsql php5-tidy php5-curl php-xml-parser unzip

RUN a2enmod rewrite

ADD http://releases.taotesting.com/TAO_2.6.5_build.zip /tmp/TAO_2.6.5_build.zip
#ADD TAO_2.6.5_build.zip /tmp/TAO_2.6.5_build.zip

WORKDIR /tmp

RUN unzip TAO_2.6.5_build.zip; mv TAO_2.6.5_build web; mv web /home/; chown -R www-data.www-data /home/web

ADD apache.conf /etc/apache2/sites-enabled/000-default.conf
ADD php.ini /etc/php5/apache2/php.ini

EXPOSE 80

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
