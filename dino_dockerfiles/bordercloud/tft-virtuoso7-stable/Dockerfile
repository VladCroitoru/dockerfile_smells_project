FROM centos/systemd

MAINTAINER "Karima Rafes" <karima.rafes@gmail.com>

#update the server
RUN yum -y update; yum clean all;

# -----------------------------------------------------------------------------
# Base CentOS-7, Apache , PHP 7 , mysql
# -----------------------------------------------------------------------------
RUN  rpm --force -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && rpm --force -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm \
    && rpm --rebuilddb \
    &&  yum -y groupinstall "Development Tools" \
	&& yum install -y gcc gmake autoconf automake libtool \
               flex bison gperf gawk m4 make \
               openssl openssl-devel readline-devel wget mail \
               libxml2-devel libuuid-devel uuid-devel \
               ImageMagick ImageMagick-devel openldap-devel \
               libssl-dev libreadline-dev net-tools git \
	&& rm -rf /var/cache/yum/* \
	&& yum clean all

#build virtuoso
RUN  git clone --depth 1 -b stable/7 git://github.com/openlink/virtuoso-opensource.git \
    && cd virtuoso-opensource \
    && export CFLAGS="-O2 -m64" \
    && ./autogen.sh \
    && ./configure --prefix=/usr/local/virtuoso \
            --enable-ods-vad \
            --with-readline \
            && make \
            && make install

RUN  ln -s /usr/local/virtuoso/bin/virtuoso-t /usr/bin/virtuoso-t  2>&1 || true \
&& ln -s /usr/local/virtuoso/bin/isql /usr/bin/isql  2>&1 || true \
&& mkdir /data \
&& cp /usr/local/virtuoso/var/lib/virtuoso/db/virtuoso.ini /data/virtuoso.ini \
&& sed -i 's/\/usr\/local\/virtuoso\/var\/lib\/virtuoso\/db/\/data/' /data/virtuoso.ini

RUN { \
		echo '#!/bin/sh'; \
		echo '# description: Script to start the server Virtuoso'; \
		echo ''; \
		echo 'DBAPASSWORD="dba"'; \
		echo 'CONFIGFILE="/data/virtuoso.ini"'; \
		echo '#INITBD="/data/init.sql"'; \
		echo ''; \
		echo 'virtuoso-t -c $CONFIGFILE +wait'; \
		echo '#isql 1111 dba $DBAPASSWORD $INITBD'; \
	} >> /data/start.sh

RUN { \
		echo '#!/bin/sh'; \
		echo '# description: Script to stop the server Virtuoso'; \
		echo ' '; \
		echo 'DBAPASSWORD="dba"'; \
		echo ' '; \
		echo 'isql 1111 dba $DBAPASSWORD -K'; \
		echo 'sleep 5'; \
		} >> /data/stop.sh

RUN { \
		echo ''; \
		echo '[Unit]'; \
		echo 'Description=Virtuoso Open-Source server daemon'; \
		echo 'After=network.target'; \
		echo ''; \
		echo '[Service]'; \
		echo 'Type=simple'; \
		echo 'Restart=always'; \
		echo 'RestartSec=5'; \
		echo 'ExecStart=/usr/bin/virtuoso-t -f -c /data/virtuoso.ini +wait'; \
		echo 'ExecReload=/data/stop.sh'; \
		echo 'ExecStop=/data/stop.sh'; \
		echo 'PrivateTmp=true'; \
		echo ''; \
		echo '[Install]'; \
		echo 'WantedBy=multi-user.target'; \
	} >> /etc/systemd/system/virtuoso.service

RUN chmod +x /data/start.sh \
	&& chmod +x /data/stop.sh \
	&& systemctl enable virtuoso

RUN { \
		echo ''; \
		echo 'GRANT ALL PRIVILEGES TO "SPARQL";'; \
	} >> /data/virtuoso_init.sql

RUN virtuoso-t -c /data/virtuoso.ini +wait \
	&& isql 1111 dba dba /data/virtuoso_init.sql \
	&& isql 1111 dba dba -K \
	&& sleep 5

EXPOSE 8890

RUN  yum install -y python-docutils automake autoconf libtool ncurses-devel libxslt groff pcre-devel pkgconfig \
    && cd /tmp \
	&& wget https://packagecloud.io/install/repositories/varnishcache/varnish66/script.rpm.sh \
    && chmod +x ./script.rpm.sh \
    && ./script.rpm.sh \
    && yum install -y varnish varnish-devel \
	&& yum clean all

RUN  cd /tmp \
	&& git clone --depth 1 --branch 6.6 https://github.com/varnish/varnish-modules.git \
    && cd varnish-modules \
    && ./bootstrap  \
    && ./configure \
    && make \
    && make install 
        
COPY varnish.service /etc/systemd/system
COPY default.vcl /etc/varnish/default.vcl

RUN systemctl enable varnish

RUN virtuoso-t -h || (exit 0)

EXPOSE 80

CMD ["/usr/sbin/init"]
