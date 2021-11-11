FROM alpine as ioncube_loader
RUN apk add git \
	&& git -c http.sslVerify=false clone https://git.dev.glo.gb/cloudhostingpublic/ioncube_loader \
	&& tar zxf ioncube_loader/ioncube_loaders_lin_x86-64.tar.gz

FROM 1and1internet/ubuntu-16-apache
MAINTAINER brian.wojtczak@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
ARG PHP_VERSION=7.1
COPY files /
RUN \
    apt-get update && \
    apt-get install -y software-properties-common python-software-properties && \
    add-apt-repository -y -u ppa:ondrej/php && \
    apt-get update && \
    apt-get install -y imagemagick graphicsmagick && \
    apt-get install -y libapache2-mod-php${PHP_VERSION} \
                        php${PHP_VERSION}-bcmath \
                        php${PHP_VERSION}-bz2 \
                        php${PHP_VERSION}-cli \
                        php${PHP_VERSION}-common \
                        php${PHP_VERSION}-curl \
                        php${PHP_VERSION}-dba \
                        php${PHP_VERSION}-gd \
                        php${PHP_VERSION}-gmp \
                        php${PHP_VERSION}-imap \
                        php${PHP_VERSION}-intl \
                        php${PHP_VERSION}-ldap \
                        php${PHP_VERSION}-mbstring \
                        php${PHP_VERSION}-mcrypt \
                        php${PHP_VERSION}-mysql \
                        php${PHP_VERSION}-odbc \
                        php${PHP_VERSION}-pgsql \
                        php${PHP_VERSION}-recode \
                        php${PHP_VERSION}-snmp \
                        php${PHP_VERSION}-soap \
                        php${PHP_VERSION}-sqlite \
                        php${PHP_VERSION}-tidy \
                        php${PHP_VERSION}-xml \
                        php${PHP_VERSION}-xmlrpc \
                        php${PHP_VERSION}-xsl \
                        php${PHP_VERSION}-zip \
                        php${PHP_VERSION}-imagick && \
    apt-get install -y php-gnupg php-mongodb php-streams php-fxsl && \
    sed -i -e 's/max_execution_time = 30/max_execution_time = 300/g' /etc/php/${PHP_VERSION}/apache2/php.ini && \
    sed -i -e 's/upload_max_filesize = 2M/upload_max_filesize = 256M/g' /etc/php/${PHP_VERSION}/apache2/php.ini && \
    sed -i -e 's/post_max_size = 8M/post_max_size = 512M/g' /etc/php/${PHP_VERSION}/apache2/php.ini && \
    sed -i -e 's/memory_limit = 128M/memory_limit = 512M/g' /etc/php/${PHP_VERSION}/apache2/php.ini && \
    sed -i -e 's/DirectoryIndex index.html index.cgi index.pl index.php index.xhtml index.htm/DirectoryIndex index.php index.html index.cgi index.pl index.xhtml index.htm/g' /etc/apache2/mods-available/dir.conf && \
    sed -i -r 's/MaxConnectionsPerChild\s+0/MaxConnectionsPerChild   ${MAXCONNECTIONSPERCHILD}/' /etc/apache2/mods-available/* && \
	sed -i -e 's/^session.gc_probability = 0/session.gc_probability = 1/' \
		   -e 's/^session.gc_divisor = 1000/session.gc_divisor = 100/' /etc/php/${PHP_VERSION}/*/php.ini && \
    mkdir /tmp/composer/ && \
    cd /tmp/composer && \
    curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    chmod a+x /usr/local/bin/composer && \
    cd / && \
    rm -rf /tmp/composer && \
    apt-get remove -y python-software-properties software-properties-common && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    chmod 777 -R /var/www && \
    apache2ctl -t && \
    mkdir -p /run /var/lib/apache2 /var/lib/php && \
    chmod -R 777 /run /var/lib/apache2 /var/lib/php /etc/php/${PHP_VERSION}/apache2/php.ini

COPY --from=ioncube_loader /ioncube/ioncube_loader_lin_${PHP_VERSION}.so /usr/lib/php/20160303/
