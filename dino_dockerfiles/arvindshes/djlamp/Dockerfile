FROM debian:stretch

ENV DEBIAN_FRONTEND noninteractive

ENV APACHE_CONFDIR /etc/apache2
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV WWW_ROOT_DIR /var/www/html
ENV MYSQL_MAJOR 5.7
ENV MYSQL_VERSION 5.7.19-1debian9
ENV MYSQL_ROOT_PASSWORD my-secret-pw
ENV MYSQL_DATADIR /var/lib/mysql
ENV MYSQL_RUN_USER mysql
ENV MYSQL_RUN_GROUP mysql

RUN groupadd -r $MYSQL_RUN_GROUP && \
    useradd -r -g $MYSQL_RUN_GROUP $MYSQL_RUN_USER

RUN apt-get update && apt-get install -y --no-install-recommends \
		apache2 php7.0 wget ca-certificates gnupg2 dirmngr gosu supervisor \
		pwgen openssl perl php7.0-mysql php7.0-mbstring php7.0-mcrypt \
        php7.0-json php7.0-gd php7.0-curl php7.0-common php7.0-bz2 \
        libapache2-mod-php7.0 libphp7.0-embed php7.0-bcmath curl php7.0-cli \
        php7.0-xml php7.0-mbstring php7.0-zip php7.0-apcu git \
	&& rm -rf /var/lib/apt/lists/*

COPY mysql_pubkey.asc /mysql_pubkey.asc

RUN set -ex; \
	key='A4A9406876FCBD3C456770C88C718D3B5072E1F5'; \
	gpg --import /mysql_pubkey.asc; \
    gpg --export "$key" > /etc/apt/trusted.gpg.d/mysql.gpg; \
	apt-key list > /dev/null

RUN echo "deb http://repo.mysql.com/apt/debian/ stretch mysql-${MYSQL_MAJOR}" \
    > /etc/apt/sources.list.d/mysql.list

RUN { \
		echo mysql-community-server mysql-community-server/data-dir select ''; \
		echo mysql-community-server mysql-community-server/root-pass password ''; \
		echo mysql-community-server mysql-community-server/re-root-pass password ''; \
		echo mysql-community-server mysql-community-server/remove-test-db select false; \
	} | debconf-set-selections \
	&& apt-get update && apt-get install -y mysql-server="${MYSQL_VERSION}" \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf $MYSQL_DATADIR && mkdir -p $MYSQL_DATADIR /var/run/mysqld \
	&& chown -R $MYSQL_RUN_USER:$MYSQL_RUN_GROUP $MYSQL_DATADIR \
	    /var/run/mysqld \
# ensure that /var/run/mysqld (used for socket and lock files) is writable
# regardless of the UID our mysqld instance ends up having at runtime
	&& chmod 777 /var/run/mysqld

RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/servername.conf
# Apache + PHP requires preforking Apache for best results
RUN a2enconf servername && a2dismod mpm_event && a2enmod mpm_prefork
RUN a2enmod rewrite

RUN set -ex \
	\
# generically convert lines like
#   export APACHE_RUN_USER=www-data
# into
#   : ${APACHE_RUN_USER:=www-data}
#   export APACHE_RUN_USER
# so that they can be overridden at runtime ("-e APACHE_RUN_USER=...")
	&& sed -ri 's/^export ([^=]+)=(.*)$/: ${\1:=\2}\nexport \1/' "$APACHE_ENVVARS" \
	\
# setup directories and permissions
	&& . "$APACHE_ENVVARS" \
	&& for dir in \
		"$APACHE_LOCK_DIR" \
		"$APACHE_RUN_DIR" \
		"$APACHE_LOG_DIR" \
		"$WWW_ROOT_DIR" \
	; do \
		rm -rvf "$dir" \
		&& mkdir -p "$dir" \
		&& chown -R "$APACHE_RUN_USER:$APACHE_RUN_GROUP" "$dir"; \
	done

# logs should go to stdout / stderr
RUN set -ex \
	&& . "$APACHE_ENVVARS" \
	&& ln -sfT /dev/stderr "$APACHE_LOG_DIR/error.log" \
	&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/access.log" \
	&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/other_vhosts_access.log"

# the "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't
# have an explicit way to disable the mysql_install_db codepath besides having
# a database already "configured" (ie, stuff in /var/lib/mysql/mysql)
# also, we set debconf keys to make APT a little quieter

# comment out a few problematic configuration values
# don't reverse lookup hostnames, they are usually another container
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/mysql.conf.d/mysqld.cnf \
	&& echo '[mysqld]\nskip-host-cache\nskip-name-resolve' > /etc/mysql/conf.d/docker.cnf

VOLUME $MYSQL_DATADIR

WORKDIR $WWW_ROOT_DIR
EXPOSE 80
EXPOSE 3306

ADD https://www.adminer.org/latest-mysql-en.php $WWW_ROOT_DIR/adminer/index.php
RUN chmod 644 $WWW_ROOT_DIR/adminer/index.php

ADD https://getcomposer.org/installer /var/www/html/composer-setup.php
RUN php composer-setup.php --install-dir=/usr/bin --filename=composer

COPY setup $WWW_ROOT_DIR/setup
COPY *.sh /usr/local/bin/
COPY *.conf /etc/supervisor/conf.d/

ENTRYPOINT ["entrypoint.sh"]

CMD ["mysqld"]
