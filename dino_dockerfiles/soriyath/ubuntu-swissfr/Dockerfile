FROM ubuntu:xenial
MAINTAINER Sumi Straessle

# NB ntp is set in base VM (host on linux hosts, most likely boot2docker on Windows and Mac)
# Time of the containers is the time of the host machine

# Set the locale (Debian removed dependency to locale in 2011)
RUN DEBIAN_FRONTEND=noninteractive apt-get update \
	&& apt-get install -y software-properties-common vim less locales locales-all \
	&& echo "fr_CH.UTF-8 UTF-8" > /etc/locale.gen \
	&& locale-gen fr_CH.UTF-8 \
	&& update-locale LANG=fr_CH.UTF-8 \
	&& cp /usr/share/zoneinfo/Europe/Zurich /etc/localtime \
	&& echo "Europe/Zurich" > /etc/timezone \
	&& DEBIAN_FRONTEND=noninteractive dpkg-reconfigure -f noninteractive tzdata \
	&& printf 'LANG=fr_CH.utf8\nLANGUAGE=fr_CH:fr\nLC_CTYPE="fr_CH.utf8"\nLC_ALL=fr_CH.utf8'>/etc/default/locale 

ENV LANG fr_CH.UTF-8  
ENV LANGUAGE fr_CH:fr
ENV LC_ALL fr_CH.UTF-8 

# Clean
RUN DEBIAN_FRONTEND=noninteractive apt-get clean \
	&& apt-get autoremove \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ['bash']
