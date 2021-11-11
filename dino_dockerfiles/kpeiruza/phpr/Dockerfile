FROM	debian:stretch
MAINTAINER kenneth@floss.cat
RUN	sed -i "s/main$/\0 contrib/" /etc/apt/sources.list && \
	apt-get update && apt-get -y upgrade && \
	apt-get -y install libapache2-mod-php7.0 php-mysql php-gd && \
	rm -f /var/cache/apt/archives/*.deb && \
	ln -sf /dev/stdout /var/log/apache2/access.log && \
	ln -sf /dev/sterr /var/log/apache2/error.log
ENTRYPOINT [ "/usr/sbin/apachectl", "-D FOREGROUND" ]
