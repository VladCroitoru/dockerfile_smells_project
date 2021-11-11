FROM soriyath/debian-swissfr
MAINTAINER Sumi Straessle

ENV DEBIAN_FRONTEND noninteractive
ENV VERSION 8.9.4

RUN	DEBIAN_FRONTEND=noninteractive set -ex \
	&& apt-get update \
	&& apt-get install -y build-essential --no-install-recommends
WORKDIR /usr/local/src
RUN wget https://nodejs.org/dist/v${VERSION}/node-v${VERSION}.tar.gz \
	&& tar -xzf node-v${VERSION}.tar.gz && rm -f node-v${VERSION}.tar.gz \
	&& cd node-v${VERSION} \
	&& ./configure \
	&& make -j $(cat /proc/cpuinfo | grep processor | wc -l)\
	&& make install

# removing extraneous packages
RUN apt-get purge -y --auto-remove build-essential

RUN apt-get clean \
	&& apt-get autoremove \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /srv/app
EXPOSE 27017 28017

# default command
CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
