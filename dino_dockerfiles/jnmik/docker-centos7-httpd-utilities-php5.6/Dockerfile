FROM jnmik/docker-centos7-httpd-utilities:latest
MAINTAINER Jean-Michael Cyr <cyrjeanmichael@gmail.com>

# Update repo for php 5.6
#RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/epel-release.rpm
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
RUN rpm -Uvh http://download.newrelic.com/pub/newrelic/el5/i386/newrelic-repo-5-3.noarch.rpm
RUN yum -y update && yum -y install php56w php56w-mysql php56w-xml php56w-mbstring php56w-opcache newrelic-sysmond newrelic-php5 && yum -y clean all
RUN sed -i "s/short_open_tag = .*/short_open_tag = On/" /etc/php.ini

# Add newrelic support
ENV NR_INSTALL_SILENT 1
ADD prepare-newrelic.sh /prepare-newrelic.sh
RUN chmod +x /prepare-newrelic.sh