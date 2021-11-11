FROM ubuntu:16.04
MAINTAINER      yakeworld "yakeworld@gmail.com"
# Make sure we don't get notifications we can't answer during building.
ENV     DEBIAN_FRONTEND noninteractive
RUN apt-get -q update \
&&  apt-get  -yq  install apache2 openssl libapache2-mod-perl2 locales\
&&  apt-get -yq install build-essential libcrypt-ssleay-perl libnet-ssleay-perl libcompress-raw-lzma-perl libio-compress-lzma-perl wget libyaml-perl libconfig-yaml-perl fcgiwrap spawn-fcgi libfcgi-perl  libfcgi-procmanager-perl perl-modules libnet-ssleay-perl libcrypt-ssleay-perl liburi-perl libjson-perl libjavascript-minifier-xs-perl libperlio-gzip-perl libmodule-install-perl libmodule-build-perl liblocal-lib-perl libjson-pp-perl libcpan-meta-perl libdbd-sqlite3 libdbd-sqlite3-perl libcurl4-nss-dev get-flash-videos libdbd-mysql-perl \
&&  a2enmod cgid \ 
&&  mkdir /var/www/perl \
&&  wget https://raw.githubusercontent.com/yakeworld/cgiproxy/master/000-default.conf -O /etc/apache2/sites-enabled/000-default.conf \
&&  wget https://raw.githubusercontent.com/yakeworld/cgiproxy/master/apache2.conf -O /etc/apache2/apache2.conf \
&&  wget https://raw.githubusercontent.com/yakeworld/cgiproxy/master/readme.pl -O /var/www/perl/readme.pl \
&&  chmod a+x /var/www/perl/readme.pl \
&&  sed -i 's/^ServerSignature/#ServerSignature/g' /etc/apache2/conf-enabled/security.conf; \
    sed -i 's/^ServerTokens/#ServerTokens/g' /etc/apache2/conf-enabled/security.conf; \
    echo "ServerSignature Off" >> /etc/apache2/conf-enabled/security.conf; \
    echo "ServerTokens Prod" >> /etc/apache2/conf-enabled/security.conf; \
    a2enmod ssl; \
    a2enmod headers; \
    echo "SSLProtocol ALL -SSLv2 -SSLv3" >> /etc/apache2/apache2.conf \
&&  service apache2 start \
&&  locale-gen en_US en_US.UTF-8 \
&&  apt-get clean ; rm -rf /tmp/* /var/tmp/* ; rm -rf /var/lib/apt/lists/* ; rm -f /etc/dpkg/dpkg.cfg.d/02apt-speedup  \
&&  cd /var/www/html \
&& wget http://www.jmarshall.com/tools/cgiproxy/releases/cgiproxy.latest.tar.gz && tar zxf cgiproxy.latest.tar.gz \
&&  chmod a+x nph-proxy.cgi ; ./nph-proxy.cgi install-modules  \
&&  rm /var/www/html/cgiproxy.latest.tar.gz

    
#WORKDIR /var/www/html
#CMD     ["/bin/bash", "-c", "sudo -u www-data ./nph-proxy.cgi start-fcgi"]
