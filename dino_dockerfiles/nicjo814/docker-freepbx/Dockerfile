FROM phusion/baseimage

# Set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV HOME="/root"
ENV TERM=xterm
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8
ENV ASTERISKUSER asterisk
ENV ASTERISK_DB_PW Password
ENV ASTERISKVER 13.1
ENV FREEPBXVER 12.0.43

EXPOSE 80

CMD ["/sbin/my_init"]

# Setup services
COPY start-apache2.sh /etc/service/apache2/run
COPY start-mysqld.sh /etc/service/mysqld/run
COPY start-asterisk.sh /etc/service/asterisk/run
COPY start-amportal.sh /etc/my_init.d/10_amportal.sh
COPY start-fail2ban.sh /etc/my_init.d/20_fail2ban.sh

RUN chmod +x /etc/service/apache2/run && \
    chmod +x /etc/service/mysqld/run && \
    chmod +x /etc/service/asterisk/run && \
    chmod +x /etc/my_init.d/10_amportal.sh && \
    chmod +x /etc/my_init.d/20_fail2ban.sh

# Following steps on FreePBX wiki
# http://wiki.freepbx.org/display/HTGS/Installing+FreePBX+12+on+Ubuntu+Server+14.04+LTS

# Install Required Dependencies
RUN sed -i 's/archive.ubuntu.com/mirrors.digitalocean.com/' /etc/apt/sources.list && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        apache2 \
        automake \
        bison \
        build-essential \
        curl \
        fail2ban \
        flex \
        libasound2-dev \
        libcurl4-openssl-dev \
        libical-dev \
        libmyodbc \
        libmysqlclient-dev \
        libncurses5-dev \
        libneon27-dev \
        libnewt-dev \
        libogg-dev \
        libspandsp-dev \
        libsrtp0-dev \
        libssl-dev \
        libsqlite3-dev \
        libtool \
        libvorbis-dev \
        libxml2-dev \
        mpg123 \
        mysql-client \
        mysql-server \
        php5 \
        php5-cli \
        php5-curl \
        php-db \
        php5-gd \
        php5-mysql \
        php-pear \
        pkg-config \
        sox\
        sqlite3 \
        autoconf \
        subversion \
        unixodbc-dev \
        uuid \
        uuid-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mv /etc/fail2ban/filter.d/asterisk.conf /etc/fail2ban/filter.d/asterisk.conf.org && \
    mv /etc/fail2ban/jail.conf /etc/fail2ban/jail.conf.org

# Copy new fail2ban config for asterisk 13
COPY conf/fail2ban/asterisk.conf /etc/fail2ban/filter.d/asterisk.conf
COPY conf/fail2ban/jail.conf /etc/fail2ban/jail.conf

# Replace default conf files to reduce memory usage
COPY conf/my-small.cnf /etc/mysql/my.cnf
COPY conf/mpm_prefork.conf /etc/apache2/mods-available/mpm_prefork.conf

# Install PearDB
RUN pear uninstall db && \
    pear install db-1.7.14

# Compile and install pjproject
WORKDIR /usr/src
RUN curl -sf -o pjproject.tar.bz2 -L http://www.pjsip.org/release/2.3/pjproject-2.3.tar.bz2 && \
    mkdir pjproject && \
    tar -xf pjproject.tar.bz2 -C pjproject --strip-components=1 && \
    rm pjproject.tar.bz2 && \
    cd pjproject && \
    ./configure --enable-shared --disable-sound --disable-resample --disable-video --disable-opencore-amr && \
    make dep && \
    make && \
    make install && \
    rm -r /usr/src/pjproject

# Compile and Install jansson
WORKDIR /usr/src
RUN curl -sf -o jansson.tar.gz -L http://www.digip.org/jansson/releases/jansson-2.7.tar.gz && \
    mkdir jansson && \
    tar -xzf jansson.tar.gz -C jansson --strip-components=1 && \
    rm jansson.tar.gz && \
    cd jansson && \
    autoreconf -i && \
    ./configure && \
    make && \
    make install && \
    rm -r /usr/src/jansson

# Compile and Install Asterisk
WORKDIR /usr/src
RUN curl -sf -o asterisk.tar.gz -L http://downloads.asterisk.org/pub/telephony/certified-asterisk/certified-asterisk-$ASTERISKVER-current.tar.gz && \
    mkdir asterisk && \
    tar -xzf /usr/src/asterisk.tar.gz -C /usr/src/asterisk --strip-components=1 && \
    rm asterisk.tar.gz && \
    cd asterisk && \
    ./configure && \
    contrib/scripts/get_mp3_source.sh && \
    make menuselect.makeopts && \
    menuselect/menuselect --enable chan_sip menuselect.makeopts && \
    sed -i "s/BUILD_NATIVE//" menuselect.makeopts && \
    make && \
    make install && \
    make config && \
    ldconfig && \
    rm -r /usr/src/asterisk

# Download extra sounds
WORKDIR /var/lib/asterisk/sounds
RUN curl -sf -o asterisk-extra-sounds-en-wav-current.tar.gz -L http://downloads.asterisk.org/pub/telephony/sounds/asterisk-extra-sounds-en-wav-current.tar.gz && \
    tar -xzf asterisk-extra-sounds-en-wav-current.tar.gz && \
    rm -f asterisk-extra-sounds-en-wav-current.tar.gz && \
    curl -sf -o asterisk-extra-sounds-en-g722-current.tar.gz -L http://downloads.asterisk.org/pub/telephony/sounds/asterisk-extra-sounds-en-g722-current.tar.gz && \
    tar -xzf asterisk-extra-sounds-en-g722-current.tar.gz && \
    rm -f asterisk-extra-sounds-en-g722-current.tar.gz

# Add Asterisk user
RUN useradd -m $ASTERISKUSER && \
    chown $ASTERISKUSER. /var/run/asterisk && \ 
    chown -R $ASTERISKUSER. /etc/asterisk && \
    chown -R $ASTERISKUSER. /var/lib/asterisk && \
    chown -R $ASTERISKUSER. /var/log/asterisk && \
    chown -R $ASTERISKUSER. /var/spool/asterisk && \
    chown -R $ASTERISKUSER. /usr/lib/asterisk && \
    chown -R $ASTERISKUSER. /var/www/ && \
    chown -R $ASTERISKUSER. /var/www/* && \
    rm -rf /var/www/html

# Configure apache
RUN sed -i 's/\(^upload_max_filesize = \).*/\120M/' /etc/php5/apache2/php.ini && \
    cp /etc/apache2/apache2.conf /etc/apache2/apache2.conf_orig && \
    sed -i 's/^\(User\|Group\).*/\1 asterisk/' /etc/apache2/apache2.conf && \
    sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf

# Configure Asterisk database in MYSQL
RUN /etc/init.d/mysql start && \
    mysqladmin -u root create asterisk && \
    mysqladmin -u root create asteriskcdrdb && \
    mysql -u root -e "GRANT ALL PRIVILEGES ON asterisk.* TO $ASTERISKUSER@localhost IDENTIFIED BY '$ASTERISK_DB_PW';" && \
    mysql -u root -e "GRANT ALL PRIVILEGES ON asteriskcdrdb.* TO $ASTERISKUSER@localhost IDENTIFIED BY '$ASTERISK_DB_PW';" && \
    mysql -u root -e "flush privileges;"
    

# Download and install FreePBX
WORKDIR /usr/src
RUN curl -sf -o freepbx-$FREEPBXVER.tgz -L http://mirror.freepbx.org/freepbx-$FREEPBXVER.tgz && \
    tar xfz freepbx-$FREEPBXVER.tgz && \
    rm freepbx-$FREEPBXVER.tgz && \
    cd /usr/src/freepbx && \
    /etc/init.d/mysql start && \
    /etc/init.d/apache2 start && \
    /usr/sbin/asterisk && \
    ./install_amp --installdb --username=$ASTERISKUSER --password=$ASTERISK_DB_PW && \
    amportal chown && \
    amportal a ma upgrade framework && \
    amportal a ma upgradeall && \
    amportal chown && \
    amportal a reload && \
    amportal a ma refreshsignatures && \
    amportal chown && \
    mysql -u$ASTERISKUSER -p$ASTERISK_DB_PW asterisk -e "INSERT into logfile_logfiles \
        (name, debug, dtmf, error, fax, notice, verbose, warning, security) \
        VALUES ('fail2ban', 'off', 'off', 'on', 'off', 'on', 'off', 'on', 'on');" && \
    amportal a r && \
    ln -s /var/lib/asterisk/moh /var/lib/asterisk/mohmp3 && \
    rm -r /usr/src/freepbx

#Make CDRs work
COPY conf/cdr/odbc.ini /etc/odbc.ini
COPY conf/cdr/odbcinst.ini /etc/odbcinst.ini
COPY conf/cdr/cdr_adaptive_odbc.conf /etc/asterisk/cdr_adaptive_odbc.conf
RUN chown asterisk:asterisk /etc/asterisk/cdr_adaptive_odbc.conf && \
    chmod 775 /etc/asterisk/cdr_adaptive_odbc.conf

WORKDIR /
