FROM ubuntu
MAINTAINER Yago Silvela 

#######################  NODE
RUN apt-get update
RUN apt-get install -y nodejs

#######################  MONGO JS

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		ca-certificates curl \
		numactl \
	&& rm -rf /var/lib/apt/lists/*

# grab gosu for easy step-down from root
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
	&& curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
	&& gpg --verify /usr/local/bin/gosu.asc \
	&& rm /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu

# gpg: key 7F0CEB10: public key "Richard Kreuter <richard@10gen.com>" imported
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 492EAFE8CD016A07919F1D2B9ECBEC467F0CEB10

ENV MONGO_MAJOR 3.0
ENV MONGO_VERSION 3.0.2

RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/$MONGO_MAJOR main" > /etc/apt/sources.list.d/mongodb-org.list

RUN set -x \
	&& apt-get update \
	&& apt-get install -y mongodb-org=$MONGO_VERSION \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/lib/mongodb \
	&& mv /etc/mongod.conf /etc/mongod.conf.orig

RUN mkdir -p /data/db && chown -R mongodb:mongodb /data/db
VOLUME /data/db

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 27017

CMD ["mongod"]

ENV MONGO_HOST 127.0.0.1
ENV MONGO_PORT 27017

#########################    APACHE
# install required
RUN apt-get install -q -y build-essential apache2 php5 libapache2-mod-php5 php5-dev php-pear wget unzip

# set environment variables for apache
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

# check php.ini
#RUN php --ini

######################  MONGO DRIVERS FOR APACHE
RUN pecl install mongo
#RUN echo "extension=mongo.so" >> /etc/php5/apache2/php.ini
RUN touch /etc/php5/conf.d/mongo.ini
RUN echo "extension=mongo.so" >> /etc/php5/conf.d/mongo.ini

####################### ROCKMONGO

RUN cd /root && wget --no-check-certificate https://github.com/gilacode/rockmongo/archive/master.zip -O rockmongo-master.zip
RUN cd /root && unzip rockmongo-master.zip -d /var/ && rm -fr /var/www && mv /var/rockmongo-master/ /var/www
#RUN cd /var/www && ls -al

# increase php upload size
RUN sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 10M/g' /etc/php5/apache2/php.ini
RUN sed -i 's/post_max_size = 2M/post_max_size = 10M/g' /etc/php5/apache2/php.ini

#RUN cat /etc/php5/apache2/php.ini | grep mongo.so
RUN cat /etc/php5/conf.d/mongo.ini | grep mongo.so

#RUN echo '<?php phpInfo(); ?>' > /var/www/html/info.php

COPY config.php /var/www/html/config.php

####################   LAST

ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGROUND"]

ADD . /var/www

RUN cd /var/www ; npm install 


