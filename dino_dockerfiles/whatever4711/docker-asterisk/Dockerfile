FROM phusion/baseimage:0.9.18
MAINTAINER Marcel Großmann <whatever4711@gmail.com>

# Set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV ASTERISKUSER asterisk
CMD ["/sbin/my_init"]

COPY scripts /usr/src
COPY conf /usr/conf
WORKDIR /usr/src
RUN chmod +x /usr/src/install/*.sh && \
    chmod +x /usr/src/init/*.sh && \
		mkdir -p /etc/service/apache2 && \
		mkdir -p /etc/service/mysqld && \
		mkdir -p /etc/service/asterisk && \
		ln -s /usr/src/init/start-apache2.sh /etc/service/apache2/run && \
		ln -s /usr/src/init/start-mysqld.sh /etc/service/mysqld/run && \
		ln -s /usr/src/init/start-asterisk.sh /etc/service/asterisk/run && \
		ln -s /usr/src/init/start-fwconsole.sh /etc/my_init.d/start-fwconsole.sh

# *Loosely* Following steps on FreePBX wiki
# http://wiki.freepbx.org/display/FOP/Installing+FreePBX+13+on+Ubuntu+Server+14.04.2+LTS

# Install Required Dependencies
RUN apt-get -q update && \
	apt-get upgrade -yq && \
  apt-get install -yq \
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
		libmyodbc \
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
		php-pear \
		php5 \
		php5-cli \
		php5-curl \
		php5-gd \
		php5-mysql \
		pkg-config \
		sox \
		subversion \
		sqlite3 \
		unixodbc-dev \
		uuid \
		uuid-dev \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*



# Install Legacy pear requirements
RUN pear install Console_Getopt

RUN /usr/src/install/pjproject.sh
RUN	/usr/src/install/jansson.sh
RUN /usr/src/install/asterisk.sh $ASTERISKUSER

# Replace default conf files to reduce memory usage
RUN cp /usr/conf/my-small.cnf /etc/mysql/my.cnf && \
    cp /usr/conf/mpm_prefork.conf /etc/apache2/mods-available/mpm_prefork.conf && \
		cp /usr/conf/asterisk.conf /etc/asterisk/asterisk.conf

# Configure apache
RUN sed -i 's/\(^upload_max_filesize = \).*/\120M/' /etc/php5/apache2/php.ini \
	&& cp /etc/apache2/apache2.conf /etc/apache2/apache2.conf_orig \
	&& sed -i 's/^\(User\|Group\).*/\1 asterisk/' /etc/apache2/apache2.conf \
	&& sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf

# Configure Asterisk database in MYSQL
RUN /etc/init.d/mysql start \
	&& mysqladmin -u root create asterisk \
	&& mysqladmin -u root create asteriskcdrdb \
	&& mysql -u root -e "GRANT ALL PRIVILEGES ON asterisk.* TO $ASTERISKUSER@localhost IDENTIFIED BY '';" \
	&& mysql -u root -e "GRANT ALL PRIVILEGES ON asteriskcdrdb.* TO $ASTERISKUSER@localhost IDENTIFIED BY '';" \
	&& mysql -u root -e "flush privileges;"

#Make CDRs work
RUN cp /usr/conf/cdr/odbc.ini /etc/odbc.ini && \
    cp /usr/conf/cdr/odbcinst.ini /etc/odbcinst.ini && \
		cp /usr/conf/cdr/cdr_adaptive_odbc.conf /etc/asterisk/cdr_adaptive_odbc.conf
RUN chown asterisk:asterisk /etc/asterisk/cdr_adaptive_odbc.conf \
	&& chmod 775 /etc/asterisk/cdr_adaptive_odbc.conf

RUN /usr/src/install/freepbx.sh

WORKDIR /

#ENTRYPOINT ["/sbin/my_init"]
