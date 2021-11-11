FROM orboan/dcss-shellinabox-httpd
MAINTAINER Oriol Boix Anfosso <dev@orboan.com>

RUN \ 
rpm -Uvh --replacepkgs https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN \
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

RUN yum install -y php56w php56w-opcache php56w-mysql php56w-iconv php56w-mbstring php56w-curl php56w-openssl php56w-tokenizer php56w-soap php56w-ctype php56w-zip php56w-gd php56w-simplexml php56w-spl php56w-pcre php56w-dom php56w-xml php56w-intl php56w-json php56w-ldap php56w-pecl-apcu php56w-odbc php56w-pear php56w-xmlrpc php56w-snmp php56w-pdo curl

RUN yum install -y ghostscript

# - Clean YUM caches to minimise Docker image size...
RUN \
  yum clean all && rm -rf /tmp/yum*
 
ENV USER=www
ENV PASSWORD=iaw

VOLUME /data/www/html

ADD container-files /
