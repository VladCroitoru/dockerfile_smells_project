FROM alpine as ioncube_loader
RUN apk add git \
	&& git -c http.sslVerify=false clone https://git.dev.glo.gb/cloudhostingpublic/ioncube_loader \
	&& tar zxf ioncube_loader/ioncube_loaders_lin_x86-64.tar.gz

FROM 1and1internet/ubuntu-16-nginx
MAINTAINER brian.wojtczak@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
ARG PHP_VERSION=5.6
COPY files /
RUN \
    apt-get update && \
    apt-get install -y python-software-properties software-properties-common && \
    LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && \
    apt-get update && \
    apt-get install -y imagemagick graphicsmagick && \
    apt-get install -y php${PHP_VERSION}-bcmath php${PHP_VERSION}-bz2 php${PHP_VERSION}-cli php${PHP_VERSION}-common php${PHP_VERSION}-curl php${PHP_VERSION}-dba php${PHP_VERSION}-fpm php${PHP_VERSION}-gd php${PHP_VERSION}-gmp php${PHP_VERSION}-imap php${PHP_VERSION}-intl php${PHP_VERSION}-ldap php${PHP_VERSION}-mbstring php${PHP_VERSION}-mcrypt php${PHP_VERSION}-mysql php${PHP_VERSION}-odbc php${PHP_VERSION}-pgsql php${PHP_VERSION}-recode php${PHP_VERSION}-snmp php${PHP_VERSION}-soap php${PHP_VERSION}-sqlite php${PHP_VERSION}-tidy php${PHP_VERSION}-xml php${PHP_VERSION}-xmlrpc php${PHP_VERSION}-xsl php${PHP_VERSION}-zip && \
    apt-get install -y php-gnupg php-imagick php-mongodb php-streams php-fxsl && \
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
    rm -rf /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default && \
    sed -i -e 's/^user = www-data$/;user = www-data/g' /etc/php/${PHP_VERSION}/fpm/pool.d/www.conf && \
    sed -i -e 's/^group = www-data$/;group = www-data/g' /etc/php/${PHP_VERSION}/fpm/pool.d/www.conf && \
    sed -i -e 's/^listen.owner = www-data$/;listen.owner = www-data/g' /etc/php/${PHP_VERSION}/fpm/pool.d/www.conf && \
    sed -i -e 's/^listen.group = www-data$/;listen.group = www-data/g' /etc/php/${PHP_VERSION}/fpm/pool.d/www.conf && \
    sed -i -e 's/max_execution_time = 30/max_execution_time = 300/g' /etc/php/${PHP_VERSION}/fpm/php.ini && \
    sed -i -e 's/upload_max_filesize = 2M/upload_max_filesize = 256M/g' /etc/php/${PHP_VERSION}/fpm/php.ini && \
    sed -i -e 's/post_max_size = 8M/post_max_size = 512M/g' /etc/php/${PHP_VERSION}/fpm/php.ini && \
    sed -i -e 's/memory_limit = 128M/memory_limit = 512M/g' /etc/php/${PHP_VERSION}/fpm/php.ini && \
    sed -i -e 's/fastcgi_param  SERVER_PORT        $server_port;/fastcgi_param  SERVER_PORT        $http_x_forwarded_port;/g' /etc/nginx/fastcgi.conf && \
    sed -i -e 's/fastcgi_param  SERVER_PORT        $server_port;/fastcgi_param  SERVER_PORT        $http_x_forwarded_port;/g' /etc/nginx/fastcgi_params && \
    sed -i -e '/sendfile on;/a\        fastcgi_read_timeout 300\;' /etc/nginx/nginx.conf && \
	sed -i -e 's/^session.gc_probability = 0/session.gc_probability = 1/' \
		   -e 's/^session.gc_divisor = 1000/session.gc_divisor = 100/' /etc/php/${PHP_VERSION}/*/php.ini && \
    mkdir --mode 777 /var/run/php && \
    chmod 755 /hooks /var/www && \
    chmod -R 777 /var/www/html /var/log && \
    sed -i -e 's/index index.html/index index.php index.html/g' /etc/nginx/sites-enabled/site.conf && \
    chmod 666 /etc/nginx/sites-enabled/site.conf /etc/passwd /etc/group && \
    nginx -t && \
    mkdir -p /run /var/lib/nginx /var/lib/php && \
    chmod -R 777 /run /var/lib/nginx /var/lib/php /etc/php/${PHP_VERSION}/fpm/php.ini

COPY --from=ioncube_loader /ioncube/ioncube_loader_lin_${PHP_VERSION}.so /usr/lib/php/20131226/
