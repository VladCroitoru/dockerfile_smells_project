FROM ubuntu:saucy
MAINTAINER s. rannou <mxs@sbrk.org>

RUN echo "deb http://archive.ubuntu.com/ubuntu saucy main universe" > /etc/apt/sources.list
RUN apt-get -qq update && \
    apt-get -qq upgrade && \
    apt-get clean

ENV DEBIAN_FRONTEND noninteractive
EXPOSE 80

RUN apt-get install -qq apache2 libapache2-mod-php5 php5-sqlite && \
    apt-get clean

ADD 000-default.conf /etc/apache2/sites-available/000-default.conf
ADD bootstrap.bash /bootstrap.bash
ADD www /var/www
RUN chown -R www-data:www-data /var/www && \
    chmod -R +w /var/www/data && \
    rm /var/www/index.html && \
    a2enmod rewrite

CMD /bootstrap.bash
