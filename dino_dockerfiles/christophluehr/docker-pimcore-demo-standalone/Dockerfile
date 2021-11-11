FROM google/debian:jessie
MAINTAINER pimcore GmbH <info@pimcore.com>

RUN apt-get update && \
 DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
 DEBIAN_FRONTEND=noninteractive apt-get -y install wget sudo supervisor pwgen apt-utils

ADD sources.list /tmp/sources.list
RUN cat /tmp/sources.list > /etc/apt/sources.list 

RUN wget -O - http://www.dotdeb.org/dotdeb.gpg | apt-key add - 

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
 php7.0-fpm php7.0-cli php7.0-curl php7.0-dev php7.0-gd php7.0-imagick php7.0-imap \
 php7.0-intl php7.0-mcrypt php7.0-memcache php7.0-mysql php7.0-sqlite php7.0-redis \
 php7.0-bz2 php7.0-ldap php7.0-xml php7.0-mbstring php7.0-zip php7.0-bcmath bzip2 unzip memcached ntpdate libxrender1 libfontconfig1 \
 imagemagick inkscape build-essential libssl-dev rcconf sudo lynx autoconf \
 libmagickwand-dev pngnq pngcrush xvfb cabextract libfcgi0ldbl poppler-utils rsync \
 xz-utils libreoffice python-uno libreoffice-math xfonts-75dpi jpegoptim monit \
 aptitude pigz libtext-template-perl mailutils redis-server git-core curl \
 mariadb-server-10.0

# set root password
RUN echo "root:root" | chpasswd

# configure apache
RUN apt-get -y install apache2 libapache2-mod-fastcgi
RUN a2dismod -f cgi autoindex mpm_worker mpm_prefork
RUN a2enmod rewrite actions fastcgi alias status filter expires headers setenvif proxy proxy_fcgi socache_shmcb mpm_event ssl
RUN rm /etc/apache2/sites-enabled/* 
RUN rm -r /var/www/* 
RUN chown -R www-data:www-data /var/www
ADD vhost.conf /etc/apache2/sites-enabled/000-default.conf

# configure mysql
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf

# configure php-fpm
RUN rm -r /etc/php/7.0/cli/php.ini
RUN rm -r /etc/php/7.0/fpm/php.ini
ADD php.ini /etc/php/7.0/fpm/php.ini 
RUN ln -s /etc/php/7.0/fpm/php.ini /etc/php/7.0/cli/php.ini
RUN mv /etc/php/7.0/fpm/pool.d/www.conf /etc/php/7.0/fpm/pool.d/www.conf.dist 
ADD www-data.conf /etc/php/7.0/fpm/pool.d/www-data.conf

# configure redis
ADD redis.conf /tmp/redis.conf
RUN cat /tmp/redis.conf >> /etc/redis/redis.conf

# install tools
RUN wget "http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb" -O wkhtmltopdf-0.12.deb && dpkg -i wkhtmltopdf-0.12.deb
ADD install-ghostscript.sh /tmp/install-ghostscript.sh
ADD install-ffmpeg.sh /tmp/install-ffmpeg.sh
RUN chmod 755 /tmp/*.sh
RUN /tmp/install-ghostscript.sh
RUN /tmp/install-ffmpeg.sh 

# setup startup scripts
ADD start-apache.sh /start-apache.sh
ADD start-php-fpm.sh /start-php-fpm.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# pimcore config files
ADD cache.php /tmp/cache.php

# ports
EXPOSE 80

# volumes
VOLUME ["/var/www", "/var/lib/mysql"]

CMD ["/run.sh"]
