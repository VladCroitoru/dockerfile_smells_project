FROM phusion/baseimage:0.9.22
MAINTAINER N Panchal <zafayar@hotmail.com>

ENV PYDIO_VERSION="8.0.2"
ENV PYDIO_BOOSTER_VER="1.2.0"
ENV DEBIAN_FRONTEND=noninteractive

CMD ["/sbin/my_init"]


RUN add-apt-repository ppa:ondrej/php -y -u && \
	apt-get -q -y --no-install-recommends update && apt-get -q -y --no-install-recommends upgrade && \
	apt-get -q -y --no-install-recommends install \
	php7.0-fpm \
	php7.0-apcu \
	php7.0-bcmath \
	php7.0-bz2 \
	php7.0-calendar \
	php7.0-ctype \
	php7.0-curl \
	php7.0-dba \
	php7.0-dom \
	php7.0-exif \
	php7.0-ftp \
	php7.0-gd \
	php7.0-gettext \
	php7.0-iconv \
	php7.0-imagick \
	php7.0-imap \
	php7.0-intl \
	php7.0-json \
	php7.0-ldap \
	php7.0-mbstring \
	php7.0-mcrypt \
	php7.0-memcached \
	php7.0-mysqlnd \
	php7.0-opcache \
	php7.0-pgsql \
	php7.0-pspell \
	php7.0-sqlite3 \
	php7.0-ssh2 \
	php7.0-xml \
	php7.0-xmlrpc \
	php7.0-zip \
#	php7.0-zlib \
	zip \
	telnet \
	nginx \
	memcached \
	mysql-client && \
	apt-get -q -y --no-install-recommends purge syslog-ng* openssh-server -y && \
	apt-get -q -y --no-install-recommends clean && apt-get -q -y --no-install-recommends autoremove -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/log/* && \
	rm -rf /etc/service/sshd /etc/service/syslog-forwarder /etc/service/syslog-ng /etc/my_init.d/00_regen_ssh_host_keys.sh && \
	/usr/sbin/adduser --system --no-create-home --group abc

RUN  mkdir -p /var/www/pydio \
     && curl -SL https://download.pydio.com/pub/core/archives/pydio-core-$PYDIO_VERSION.tar.gz | tar -C /var/www/pydio --strip-components=1 -zx \
     && rm -rf /var/www/pydio/data \
     && ln -s /data/pydio /var/www/pydio/data \
     && find /var/www/pydio -name .htaccess -delete \
     && curl -o /usr/local/bin/pydio -SL https://download.pydio.com/pub/booster/release/$PYDIO_BOOSTER_VER/linux_amd64/pydio \
 	&& chmod +x /usr/local/bin/pydio


RUN rm -Rf /var/log && \
	mkdir /log && \
	ln -s /log /var/log

COPY root/ /

RUN find /etc/service -name run  | xargs chmod +x && \
	chmod +x /etc/my_init.d/* && \
	mkdir /run/php -p

EXPOSE 80 443 8090
VOLUME /data /log

ADD ./bootstrap.json /data/pydio/plugins/boot.conf/bootstrap.json
ADD ./data /var/www/data

# Use baseimage-docker's init system.
#CMD ["/bin/bash"]

