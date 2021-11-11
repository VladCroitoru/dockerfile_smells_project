FROM ronmi/ynit-image
MAINTAINER Ronmi Ren <ronmi@patrolavia.com>

# install dependencies
RUN export REQ="nginx-light mysql-server php5-cli php5-fpm php5 \
       php5-curl php5-mysql php-pear php5-gd curl wget ca-certificates \
       libmyodbc mpg123 sox uuid sudo vim-tiny cron \
       libiksemel3 libpjsua2 libjansson4 openssl lua5.1 \
       libnewt0.52 libsqlite3-0 libxslt1.1 libfreeradius-client2 libpq5 \
       libgmime-2.6-0 liblua5.1-0 libical1a libneon27 libsnmp30 libspandsp2 \
       libpci3 libglib2.0-0 libsdl1.2debian libsybdb5" \
 && export DEP="build-essential pkg-config automake libtool autoconf git subversion \
       bison flex \
       libpjproject-dev libpt-dev \
       libncurses-dev libz-dev libssl-dev libxml2-dev libsqlite3-dev uuid-dev \
       libspeex-dev libspeexdsp-dev libogg-dev libvorbis-dev libasound2-dev portaudio19-dev libcurl4-openssl-dev \
       libpq-dev unixodbc-dev libmysqlclient15-dev libneon27-dev libgmime-2.6-dev libusb-dev liblua5.1-0-dev \
       libh323plus-dev libvpb-dev libgtk2.0-dev libmysqlclient-dev libbluetooth-dev libfreeradius-client-dev freetds-dev \
       libsnmp-dev libiksemel-dev libcorosync-dev libnewt-dev libpopt-dev libical-dev libspandsp-dev libjack-dev \
       libresample-dev libc-client-dev binutils-dev libsrtp-dev libgsm1-dev libedit-dev doxygen libjansson-dev libldap-dev \
       libxslt1-dev" \
 && cp /etc/apt/sources.list /etc/apt/sources.list.bak \
 && sed -i 's/httpredir/ftp.tw/' /etc/apt/sources.list \
 && set -x \
 && apt-get update \
 && echo 'mysql-server mysql-server/root_password password secret' | debconf-set-selections \
 && echo 'mysql-server mysql-server/root_password_again password secret' | debconf-set-selections \
 && echo 'libvpb0 libvpb0/countrycode string 886' | debconf-set-selections \
 && apt-get install -y --no-install-recommends $REQ $DEP \
 && mv -f /etc/apt/sources.list.bak /etc/apt/sources.list \
 && mkdir /build \
 && mkdir /build/ast \
 && curl -sS http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-13-current.tar.gz \
       | tar zxf - --strip-components=1 -C /build/ast \
 && ( \
       cd /build/ast \
       ;  contrib/scripts/get_mp3_source.sh \
       && PTLIB_CONFIG=/usr/share/ptlib/make/ptlib-config ./configure \
       && make menuselect.makeopts \
       && menuselect/menuselect --enable format_mp3 menuselect.makeopts \
       && menuselect/menuselect --enable res_config_mysql menuselect.makeopts \
       && menuselect/menuselect --enable astman menuselect.makeopts \
       && menuselect/menuselect --disable BUILD_NATIVE menuselect.makeopts \
       && menuselect/menuselect --enable LOW_MEMORY menuselect.makeopts \
       && menuselect/menuselect --enable EXTRA-SOUNDS-EN-WAV menuselect.makeopts \
       && make \
       && make install \
       && make config \
       && make samples \
       && ldconfig \
       && sed -r -e 's/\[directories\]\(!\)/[directories]/' -i /etc/asterisk/asterisk.conf \
    ) \
 && rm -fr /build \
 && apt-get purge -y $DEP \
 && apt-get autoremove --purge -y \
 && apt-get clean -y \
 && rm -fr /var/lib/apt/lists/* \
 && adduser --gecos ,,,,, --disabled-password asterisk \
 && chown -R asterisk:asterisk /etc/asterisk /var/lib/asterisk /var/log/asterisk \
       /var/spool/asterisk /run/asterisk \
 && echo 'AST_USER="asterisk"' >> /etc/default/asterisk \
 && echo 'AST_GROUP="asterisk"' >> /etc/default/asterisk
RUN mkdir /etc/asterisk/manager.d
ADD ast_conf /etc/asterisk/
ADD admin.conf /etc/asterisk/manager.d/
ADD asterisk /etc/ynit/

# install freepbx
ADD odbc.ini odbcinst.ini /etc/
RUN mkdir -p /build/freepbx /var/lib/freepbx/cgi-bin /var/lib/freepbx/html \
 && chown -R asterisk:asterisk /var/lib/freepbx \
 && set -x \
 && curl -sS http://mirror.freepbx.org/modules/packages/freepbx/freepbx-13.0-latest.tgz | \
       tar zxf - --strip-components=1 -C /build/freepbx \
 && cd /build/freepbx \
 && service mysql restart \
 && /etc/ynit/asterisk restart \
 && sleep 5 \
 && ./install -n --no-ansi --webroot /var/lib/freepbx/html --ampcgibin /var/lib/freepbx/cgi-bin \
       --dbpass secret -f \
 && sed -i "s/amp111/$(cat /etc/amportal.conf |grep AMPMGRPASS|cut -d '=' -f 2)/" \
       /etc/asterisk/manager.d/admin.conf \
 && sudo -u asterisk fwconsole ma upgradeall \
 && sudo -u asterisk fwconsole set CHECKREFERER 0 \
 && /etc/ynit/asterisk stop \
 && service mysql stop \
 && rm -fr /build

# setup env
RUN ln -sf /etc/init.d/mysql /etc/init.d/nginx /etc/init.d/php5-fpm /etc/init.d/cron /etc/ynit/
ADD my.cnf /etc/mysql/
ADD www.conf /etc/php5/fpm/pool.d/
ADD nginx.conf /etc/nginx/

VOLUME ["/var/spool/cron/crontabs", "/var/lib/mysql", "/var/lib/asterisk", "/var/lib/freepbx/html/admin", "/var/log/asterisk", "/var/log/nginx", "/var/log/mysql", "/var/spool/asterisk", "/etc/asterisk"]
CMD ["ynit"]
