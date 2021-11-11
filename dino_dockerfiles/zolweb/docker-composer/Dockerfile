# composer image
# runs composer within a container
FROM ubuntu:14.04
MAINTAINER François Zaninotto <francois+docker@marmelab.com>, Simon Dittlmann

ENV HOME /root

RUN apt-get update -qq && \
	apt-get install -y -qq git curl && \
	apt-get -y clean

# install HHVM
RUN curl -s http://dl.hhvm.com/conf/hhvm.gpg.key | apt-key add - && \
	echo deb http://dl.hhvm.com/ubuntu trusty main | tee /etc/apt/sources.list.d/hhvm.list && \
	apt-get update -qq && \
	apt-get install -y -qq hhvm && \
	apt-get -y clean
RUN echo "date.timezone = Europe/Berlin" >> /etc/hhvm/php.ini

# install composer
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer --install-dir=/usr/local/bin

WORKDIR /srv
COPY config.hdf /etc/hhvm/config.hdf

RUN echo "alias composer='hhvm /usr/local/bin/composer'" >> /root/.bashrc

RUN hhvm /usr/local/bin/composer self-update

