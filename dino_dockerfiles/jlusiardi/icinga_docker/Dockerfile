FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

RUN \
        apt-get update; \
        apt-get install --no-install-recommends -y wget pwgen; \
        wget -O - http://packages.icinga.org/icinga.key | apt-key add -; \
        echo "deb http://packages.icinga.org/debian icinga-jessie main" > /etc/apt/sources.list.d/icinga.list; \
        echo "deb-src http://packages.icinga.org/debian icinga-jessie main" >> /etc/apt/sources.list.d/icinga.list; \
        apt-get update; \
        apt-get install -y icinga

RUN \
	apt-get install -y less vim

COPY    htpasswd.users		/etc/icinga/htpasswd.users
COPY	apache2.conf		/etc/apache2/apache2.conf
COPY	000-default.conf	/etc/apache2/sites-enabled/000-default.conf
COPY	cgid.conf		/etc/apache2/mods-enabled/cgid.conf
RUN	rm /etc/apache2/conf-enabled/other-vhosts-access-log.conf; \
	apt-get install -y supervisor;
COPY    supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY	icinga.cfg	/etc/icinga/icinga.cfg

VOLUME  ["/etc/icinga/objects"]
COPY	main.cfg	/main.cfg
COPY	start.sh	/start.sh
RUN	usermod -G nagios www-data

CMD	/bin/sh start.sh
