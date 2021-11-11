FROM ishiidaichi/docker-phalcon-nginx

MAINTAINER ishiidaichi

#install mecab
RUN apt-get -y install mecab libmecab-dev mecab-ipadic
RUN apt-get -y install aptitude
RUN aptitude -y install mecab-ipadic-utf8

#php mecab
RUN wget https://github.com/rsky/php-mecab/archive/v0.6.0.tar.gz && tar xzvf v0.6.0.tar.gz
RUN apt-get -y install re2c
RUN cd php-mecab-0.6.0/mecab && phpize && ./configure --with-mecab=/usr/bin/mecab-config && make && make install
RUN echo "extension=mecab.so" >> /etc/php5/fpm/conf.d/30-mecab.ini

EXPOSE 80 443

VOLUME ["/var/www/html"]

CMD /usr/bin/supervisord -c /etc/supervisord.conf -u root
