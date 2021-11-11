FROM soriyath/debian-postgresql94
MAINTAINER Sumi Straessle

ENV DEBIAN_FRONTEND noninteractive

# NODEJS 5.5
RUN	set -ex \
	&& apt-get update \
	&& apt-get install -y wget build-essential
WORKDIR /usr/local/src
RUN wget https://nodejs.org/dist/v5.12.0/node-v5.12.0.tar.gz \
	&& tar -xzvf node-v5.12.0.tar.gz && rm -f node-v5.12.0.tar.gz \
	&& cd node-v5.12.0 \
	&& ./configure \
	&& make -j $(cat /proc/cpuinfo | grep processor | wc -l)\
	&& make install
RUN apt-get clean \
	&& apt-get autoremove \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /srv/www

CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
