FROM soriyath/debian-swissfr
MAINTAINER Sumi Straessle

ENV DEBIAN_FRONTEND noninteractive

RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449 \
	&& echo deb http://dl.hhvm.com/debian jessie main | tee /etc/apt/sources.list.d/hhvm.list \
	&& apt-get update \
	&& apt-get install -y hhvm

RUN apt-get clean \
	&& apt-get autoremove \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /srv/www
EXPOSE 8080

# Supervisor config file
ADD hhvm.sv.conf /etc/supervisor/conf.d/hhvm.sv.conf

# default command
CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
