FROM phusion/baseimage
MAINTAINER Jason Martin <jason@greenpx.co.uk>

# Set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV ASTERISKUSER asterisk

CMD ["/sbin/my_init"]

# Setup services
COPY start-apache2.sh /etc/service/apache2/run
RUN chmod +x /etc/service/apache2/run

COPY start-mysqld.sh /etc/service/mysqld/run
RUN chmod +x /etc/service/mysqld/run

COPY start-asterisk.sh /etc/service/asterisk/run
RUN chmod +x /etc/service/asterisk/run

COPY start-amportal.sh /etc/my_init.d/start-amportal.sh

# *Loosely* Following steps on FreePBX wiki
# http://wiki.freepbx.org/display/FOP/Installing+FreePBX+13+on+Ubuntu+Server+14.04.2+LTS

# Install Required Dependencies
RUN add-apt-repository -y ppa:ondrej/php \
  && gpg --keyserver pgp.mit.edu --recv-keys 4F4EA0AAE5267A6C \
  && gpg --armor --export 4F4EA0AAE5267A6C | apt-key add - \
  && apt-get update \
  && apt-key update \
	&& apt-get upgrade -y --allow-unauthenticated \
	&& apt-get install -y --allow-unauthenticated \
		apache2 \
		autoconf \
		automake \
		bison \
		build-essential \
		curl \
		flex \
		git \
		libasound2-dev \
		libcurl4-openssl-dev \
		libical-dev \
		libmysqlclient-dev \
		libncurses5-dev \
		libneon27-dev \
		libnewt-dev \
		libodbc1 \
		libogg-dev \
		libspandsp-dev \
		libsqlite3-dev \
		libsrtp0-dev \
		libssl-dev \
		libtool \
		libvorbis-dev \
		libxml2-dev \
		mpg123 \
		mysql-client \
		mysql-server \
		openssh-server \
		php5.6 \
		php5.6-cli \
		php5.6-curl \
		php5.6-gd \
		php5.6-mbstring \
		php5.6-mysql \
    php5.6-xml \
		pkg-config \
		sox \
		subversion \
		sudo \
		sqlite3 \
		unixodbc-dev \
		uuid \
		uuid-dev \
	&& update-alternatives --set php /usr/bin/php5.6 \
	&& apt-get install -y --allow-unauthenticated php-pear \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

RUN ln -s /etc/php/5.6/ /etc/php5

# Replace default conf files to reduce memory usage
COPY conf/my-small.cnf /etc/mysql/my.cnf
COPY conf/mpm_prefork.conf /etc/apache2/mods-available/mpm_prefork.conf

# Install Legacy pear requirements
# RUN pear install Console_Getopt

# Compile and Install jansson
WORKDIR /usr/src
RUN curl -sf -o jansson.tar.gz -L http://www.digip.org/jansson/releases/jansson-2.7.tar.gz \
	&& mkdir jansson \
	&& tar -xzf jansson.tar.gz -C jansson --strip-components=1 \
	&& rm jansson.tar.gz \
	&& cd jansson \
	&& autoreconf -i \
	&& ./configure \
	&& make \
	&& make install \
	&& rm -r /usr/src/jansson

# Compile and Install Asterisk
WORKDIR /usr/src
RUN curl -sf -o asterisk.tar.gz -L http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-13-current.tar.gz \
	&& mkdir asterisk \
	&& tar -xzf /usr/src/asterisk.tar.gz -C /usr/src/asterisk --strip-components=1 \
	&& rm asterisk.tar.gz \
	&& cd asterisk \
	&& ./configure --with-pjproject-bundled \
	&& contrib/scripts/get_mp3_source.sh \
	&& make menuselect.makeopts \
	&& sed -i "s/format_mp3//" menuselect.makeopts \
	&& sed -i "s/BUILD_NATIVE//" menuselect.makeopts \
	&& make -j8 \
	&& make install \
	&& make config \
	&& ldconfig \
	&& update-rc.d -f asterisk remove \
	&& rm -r /usr/src/asterisk
COPY conf/asterisk.conf /etc/asterisk/asterisk.conf

# Download extra sounds
WORKDIR /var/lib/asterisk/sounds
RUN curl -sf -o asterisk-core-sounds-en-wav-current.tar.gz -L http://downloads.asterisk.org/pub/telephony/sounds/asterisk-core-sounds-en-wav-current.tar.gz \
	&& tar -xzf asterisk-core-sounds-en-wav-current.tar.gz \
	&& rm -f asterisk-core-sounds-en-wav-current.tar.gz \
	&& curl -sf -o asterisk-extra-sounds-en-wav-current.tar.gz -L http://downloads.asterisk.org/pub/telephony/sounds/asterisk-extra-sounds-en-wav-current.tar.gz \
	&& tar -xzf asterisk-extra-sounds-en-wav-current.tar.gz \
	&& rm -f asterisk-extra-sounds-en-wav-current.tar.gz \
	&& curl -sf -o asterisk-core-sounds-en-g722-current.tar.gz -L http://downloads.asterisk.org/pub/telephony/sounds/asterisk-core-sounds-en-g722-current.tar.gz \
	&& tar -xzf asterisk-core-sounds-en-g722-current.tar.gz \
	&& rm -f asterisk-core-sounds-en-g722-current.tar.gz \
	&& curl -sf -o asterisk-extra-sounds-en-g722-current.tar.gz -L http://downloads.asterisk.org/pub/telephony/sounds/asterisk-extra-sounds-en-g722-current.tar.gz \
	&& tar -xzf asterisk-extra-sounds-en-g722-current.tar.gz \
	&& rm -f asterisk-extra-sounds-en-g722-current.tar.gz

# Add Asterisk user
RUN useradd -m $ASTERISKUSER \
	&& chown $ASTERISKUSER. /var/run/asterisk \
	&& chown -R $ASTERISKUSER. /etc/asterisk \
	&& chown -R $ASTERISKUSER. /var/lib/asterisk \
	&& chown -R $ASTERISKUSER. /var/log/asterisk \
	&& chown -R $ASTERISKUSER. /var/spool/asterisk \
	&& chown -R $ASTERISKUSER. /usr/lib/asterisk \
	&& chown -R $ASTERISKUSER. /var/www/ \
	&& chown -R $ASTERISKUSER. /var/www/* \
	&& rm -rf /var/www/html

# Configure apache
RUN sed -i 's/\(^upload_max_filesize = \).*/\1512M/' /etc/php5/apache2/php.ini \
  && sed -i 's/\(^post_max_size = \).*/\1512M/' /etc/php5/apache2/php.ini \
	&& cp /etc/apache2/apache2.conf /etc/apache2/apache2.conf_orig \
	&& sed -i 's/^\(User\|Group\).*/\1 asterisk/' /etc/apache2/apache2.conf \
	&& sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf

# Configure Asterisk database in MYSQL
RUN /etc/init.d/mysql start && sleep 5 \
  && mysql -u root -e  "CREATE DATABASE asterisk;" \
  && echo "Asterisk DB created!" \
  && mysql -u root -e "CREATE DATABASE asteriskcdrdb;" \
  && echo "AsteriskCDR DB created!" \
  && mysql -u root -e "CREATE USER $ASTERISKUSER@localhost IDENTIFIED BY '';" \
  && echo "$ASTERISKUSER created!" \
  && mysql -u root -e "GRANT ALL PRIVILEGES ON asterisk.* TO $ASTERISKUSER@localhost IDENTIFIED BY '';" \
  && echo "Granted priviligese for $ASTERISKUSER on asterisk DB" \
  && mysql -u root -e "GRANT ALL PRIVILEGES ON asteriskcdrdb.* TO $ASTERISKUSER@localhost IDENTIFIED BY '';" \
  && echo "Granted priviligese for $ASTERISKUSER on asteriskCDR DB" \
  && mysql -u root -e "flush privileges;"

#Make CDRs work
COPY conf/cdr/odbc.ini /etc/odbc.ini
COPY conf/cdr/odbcinst.ini /etc/odbcinst.ini
COPY conf/cdr/cdr_adaptive_odbc.conf /etc/asterisk/cdr_adaptive_odbc.conf
RUN chown asterisk:asterisk /etc/asterisk/cdr_adaptive_odbc.conf \
	&& chmod 775 /etc/asterisk/cdr_adaptive_odbc.conf

# Enable Rewrite Module
RUN a2enmod rewrite

RUN apt-get update && apt-get install -y net-tools && apt-get clean

#RUN pear install Console_Getopt
# Download and install FreePBX
WORKDIR /usr/src
RUN curl -sf -o freepbx.tgz -L http://mirror.freepbx.org/modules/packages/freepbx/freepbx-13.0-latest.tgz \
	&& tar xfz freepbx.tgz \
	&& rm freepbx.tgz \
	&& cd /usr/src/freepbx \
	&& /etc/init.d/mysql start \
	&& mkdir /var/www/html \
	&& /etc/init.d/apache2 start \
	&& ./start_asterisk start \
	&& sleep 5 \
	&& sed -i "s/'0000-00-00 00:00:00'/CURRENT_TIMESTAMP/" installlib/SQL/cdr.sql \
	&& ./install -n \
	&& fwconsole restart \
	&& rm -r /usr/src/freepbx

WORKDIR /
