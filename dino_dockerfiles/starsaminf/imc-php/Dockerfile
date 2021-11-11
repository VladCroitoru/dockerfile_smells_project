FROM buildpack-deps:jessie
MAINTAINER Samuel Loza <starsaminf@gmail.com>

RUN apt-get update
RUN apt-get install -y locales apache2-bin apache2-dev apache2.2-common --no-install-recommends  
RUN apt-get install -y curl libmcrypt-dev git libxml2-dev nano libgd-dev libfreetype6-dev libjpeg62-turbo-dev libpng12-dev
RUN apt-get install -y libc-client-dev autoconf2.13 libpng-dev zlib1g-dev  zip
RUN echo America\La_Paz > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN echo 'es_BO ISO-8859-1'\
>> /etc/locale.gen &&  \
usr/sbin/locale-gen

RUN rm -rf /var/www/html && mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www/html && chown -R www-data:www-data /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www/html

# Apache + PHP requires preforking Apache for best results
RUN a2dismod mpm_event && a2enmod mpm_prefork

RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist
COPY apache2.conf /etc/apache2/apache2.conf

# compile openssl, otherwise --with-openssl won't work
RUN CFLAGS="-fPIC" && OPENSSL_VERSION="1.0.2d" \
      && cd /tmp \
      && mkdir openssl \
      && curl -sL "https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz" -o openssl.tar.gz \
      && tar -xzf openssl.tar.gz -C openssl --strip-components=1 \
      && cd /tmp/openssl \
      && ./config shared && make && make install \
      && rm -rf /tmp/*

ENV PHP_VERSION 5.3.29
ENV PHP_INI_DIR /usr/local/lib
RUN mkdir -p $PHP_INI_DIR/conf.d

# php 5.3 needs older autoconf
RUN set -x \
	&& curl -SLO http://launchpadlibrarian.net/140087283/libbison-dev_2.7.1.dfsg-1_amd64.deb \
	&& curl -SLO http://launchpadlibrarian.net/140087282/bison_2.7.1.dfsg-1_amd64.deb \
	&& dpkg -i libbison-dev_2.7.1.dfsg-1_amd64.deb \
	&& dpkg -i bison_2.7.1.dfsg-1_amd64.deb \
	&& rm *.deb \
	&& curl -SL "http://php.net/get/php-$PHP_VERSION.tar.bz2/from/this/mirror" -o php.tar.bz2 \
	&& mkdir -p /usr/src/php \
	&& tar -xf php.tar.bz2 -C /usr/src/php --strip-components=1 \
	&& rm php.tar.bz2* \
	&& cd /usr/src/php \
	&& ./buildconf --force \
	&& ./configure --disable-cgi \
		$(command -v apxs2 > /dev/null 2>&1 && echo '--with-apxs2' || true) \
    --with-config-file-path="$PHP_INI_DIR" \
    --with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \
		--with-mysql \
		--with-mysqli \
		--with-pdo-mysql \
		--with-gd \
		--with-openssl=/usr/local/ssl \
	&& make -j"$(nproc)" \
	&& make install \
	&& dpkg -r bison libbison-dev && make clean

COPY docker-php-* /usr/local/bin/
COPY apache2-foreground /usr/local/bin/
RUN docker-php-ext-install zip 
RUN docker-php-ext-install mbstring 
RUN docker-php-ext-install pdo 
RUN docker-php-ext-install pdo_mysql 
RUN docker-php-ext-install mysql 
RUN docker-php-ext-install json 
RUN docker-php-ext-install curl 
RUN docker-php-ext-install fileinfo 
#RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ 
RUN docker-php-ext-install gd
#RUN docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl 
RUN docker-php-ext-install imap
RUN docker-php-ext-install mcrypt
RUN  cp /usr/src/php/php.ini-production /usr/local/lib/php.ini
##FFmpeg
RUN wget https://raw.githubusercontent.com/q3aql/ffmpeg-install/master/ffmpeg-install
RUN chmod a+x ffmpeg-install
RUN ./ffmpeg-install --install


RUN apt-get purge -y --auto-remove autoconf2.13 
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html

EXPOSE 80
CMD ["apache2-foreground"]
