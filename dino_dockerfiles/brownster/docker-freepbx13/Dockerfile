#asterisk docker file for unraid 6
FROM phusion/baseimage:0.9.22
MAINTAINER marc brown <marc@22walker.co.uk> v0.0.2

# Set correct environment variables.
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
ENV ASTERISKUSER asterisk
ENV ASTERISKVER 13.13
ENV FREEPBXVER 13.0
ENV ASTERISK_DB_PW pass123
ENV MARIA_DB_PW pass123
ENV AUTOBUILD_UNIXTIME 1418234402
ENV FREEPBXPORT 8009
# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Add VOLUME to allow backup of FREEPBX
VOLUME ["/etc/freepbxbackup"]

# open up ports needed  by freepbx and asterisk 5060 tcp sip reg 80 tcp web port 10000-20000 udp rtp stream  
#EXPOSE 5060
#EXPOSE 80
#EXPOSE $FREEPBXPORT
#EXPOSE 10000-20000/udp

# Add start.sh
ADD start.sh /root/

#Install packages that are needed
RUN apt-get update && apt-get install -y build-essential linux-headers-generic openssh-server openssl libiksemel-dev lamp-server^ apache2 mysql-server mysql-client wget libgtk2.0-dev bison flex php5 php5-curl php5-cli php5-mysql php-pear php5-gd curl sox libncurses5-dev libssl-dev libmysqlclient-dev mpg123 libxml2-dev libnewt-dev sqlite3 libsqlite3-dev pkg-config automake libtool autoconf git unixodbc-dev uuid uuid-dev libasound2-dev libogg-dev libvorbis-dev libcurl4-openssl-dev libical-dev libneon27-dev libsrtp0-dev libspandsp-dev
# Pear install
#RUN pear install Console_Getopt \
RUN pear uninstall db 1>/dev/null \
  && pear install db-1.7.14 1>/dev/null

# add asterisk user
RUN groupadd -r $ASTERISKUSER \
 && useradd -r -g $ASTERISKUSER $ASTERISKUSER \
 && mkdir /var/lib/asterisk \
 && chown $ASTERISKUSER:$ASTERISKUSER /var/lib/asterisk \
 && usermod --home /var/lib/asterisk $ASTERISKUSER \
 && rm -rf /var/lib/apt/lists/* \
 && apt-get purge -y

# Build pj project and Build jansson
WORKDIR /temp/src/
RUN git clone https://github.com/asterisk/pjproject.git 1>/dev/null \
  && git clone https://github.com/akheron/jansson.git 1>/dev/null \
  && cd /temp/src/pjproject \
  && ./configure --enable-shared --disable-sound --disable-resample --disable-video --disable-opencore-amr 1>/dev/null \
  && make dep 1>/dev/null \
  && make 1>/dev/null \
  && make install 1>/dev/null \
  && cd /temp/src/jansson \
  && autoreconf -i 1>/dev/null \
  && ./configure 1>/dev/null \
  && make 1>/dev/null \
  && make install 1>/dev/null \
  
# Download asterisk.
# Currently Certified Asterisk 13.1.
  && curl -sf -o /tmp/asterisk.tar.gz -L http://downloads.asterisk.org/pub/telephony/certified-asterisk/certified-asterisk-$ASTERISKVER-current.tar.gz 1>/dev/null \

# gunzip asterisk
  && mkdir /usr/src/asterisk \
  && tar -xzf /tmp/asterisk.tar.gz -C /usr/src/asterisk --strip-components=1 1>/dev/null \
  && rm -f /tmp/asterisk.tar.gz 1>/dev/null
WORKDIR /usr/src/asterisk

# make asterisk.
# ENV rebuild_date 2017-12-11
# Configure
RUN ./configure --with-ssl=/opt/local --with-crypto=/opt/local 1>/dev/null \
# Remove the native build option
  && make menuselect.makeopts 1>/dev/null \
#  && sed -i "s/BUILD_NATIVE//" menuselect.makeopts 1>/dev/null \
 && menuselect/menuselect --enable chan_sip --disable BUILD_NATIVE  --enable CORE-SOUNDS-EN-WAV  --enable CORE-SOUNDS-EN-SLN16 --enable MOH-OPSOUND-WAV --enable MOH-OPSOUND-SLN16 menuselect.makeopts  menuselect.makeopts 1>/dev/null \
# Continue with a standard make.
 && make 1>/dev/null \
 && make install 1>/dev/null \
 && make config 1>/dev/null \
 && ldconfig \
#&& update-rc.d ? chkconfig asterisk off \
# aterisk sounds files
 && cd /var/lib/asterisk/sounds 1>/dev/null \
 && wget http://downloads.asterisk.org/pub/telephony/sounds/asterisk-core-sounds-en-wav-current.tar.gz 1>/dev/null \
 && wget http://downloads.asterisk.org/pub/telephony/sounds/asterisk-extra-sounds-en-wav-current.tar.gz 1>/dev/null \
 && tar xvf asterisk-core-sounds-en-wav-current.tar.gz 1>/dev/null \
 && rm -f asterisk-core-sounds-en-wav-current.tar.gz 1>/dev/null \
 && tar xfz asterisk-extra-sounds-en-wav-current.tar.gz 1>/dev/null \
 && rm -f asterisk-extra-sounds-en-wav-current.tar.gz 1>/dev/null \
# Wideband Audio download
 && wget http://downloads.asterisk.org/pub/telephony/sounds/asterisk-core-sounds-en-g722-current.tar.gz 1>/dev/null \
 && wget http://downloads.asterisk.org/pub/telephony/sounds/asterisk-extra-sounds-en-g722-current.tar.gz 1>/dev/null \
 && tar xfz asterisk-extra-sounds-en-g722-current.tar.gz 1>/dev/null \
 && rm -f asterisk-extra-sounds-en-g722-current.tar.gz 1>/dev/null \
 && tar xfz asterisk-core-sounds-en-g722-current.tar.gz 1>/dev/null \
 && rm -f asterisk-core-sounds-en-g722-current.tar.gz 1>/dev/null \

 && chown $ASRERISKUSER. /var/run/asterisk \
 && chown -R $ASTERISKUSER. /etc/asterisk \
 && chown -R $ASTERISKUSER. /var/lib/asterisk \
 && chown -R $ASTERISKUSER. /var/www/ \
 && chown -R $ASTERISKUSER. /var/www/* \
 && chown -R $ASTERISKUSER. /var/log/asterisk \
 && chown -R $ASTERISKUSER. /var/spool/asterisk \
 && chown -R $ASTERISKUSER. /var/run/asterisk \
 && chown -R $ASTERISKUSER. /var/lib/asterisk \
 && chown $ASTERISKUSER:$ASTERISKUSER /etc/freepbxbackup \
 && rm -rf /var/www/html \

#mod to apache
#Setup mysql
 && sed -i 's/\(^upload_max_filesize = \).*/\120M/' /etc/php5/apache2/php.ini \
 && cp /etc/apache2/apache2.conf /etc/apache2/apache2.conf_orig \
 && sed -i 's/^\(User\|Group\).*/\1 asterisk/' /etc/apache2/apache2.conf \
 && sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf \
 && service apache2 restart 1>/dev/null \
# && mysqladmin -u root create asterisk \
# && mysqladmin -u root create asteriskcdrdb \
# && mysql -u root -e "GRANT ALL PRIVILEGES ON asterisk.* TO $ASTERISKUSER@localhost IDENTIFIED BY '$ASTERISK_DB_PW';" \
# && mysql -u root -e "GRANT ALL PRIVILEGES ON asteriskcdrdb.* TO $ASTERISKUSER@localhost IDENTIFIED BY '$ASTERISK_DB_PW';" \
# && mysql -u root -e "flush privileges;"

#Install freepbx
WORKDIR /usr/src
RUN wget http://mirror.freepbx.org/modules/packages/freepbx/freepbx-$FREEPBXVER-latest.tgz 1>/dev/null 2>/dev/null \
 && tar vxfz freepbx-$FREEPBXVER-latest.tgz freepbx 1>/dev/null \
 && rm -f freepbx-$FREEPBXVER-latest.tgz 1>/dev/null
 
RUN /etc/init.d/mysql start 1>/dev/null \
#&& /usr/sbin/asterisk 1>/dev/null \
 && /usr/src/freepbx/start_asterisk start 1>/dev/null \
 && ./usr/src/freepbx/install -n 1>/dev/null \
 && chown -R $ASTERISKUSER. /var/lib/asterisk/bin/retrieve_conf 1>/dev/null
 
#ODBC
COPY odbc.ini /etc/
COPY odbcinst.ini /etc/
 
#for persistance
VOLUME ["/etc/asterisk","/etc/apache2","/var/www/html","/var/lib/mysql","/var/spool/asterisk","/var/lib/asterisk"]
 
#clean up
RUN find /temp -mindepth 1 -delete \
 && apt-get purge -y \
 && apt-get --yes autoremove \
 && apt-get clean all \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
   
CMD bash -C '/root/start.sh';'bash'
