FROM centos:6
MAINTAINER Liam Galvin

WORKDIR /srv

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
RUN rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm

RUN yum install -y -q git jq ant php70w php70w-xml php70w-pdo php70w-pecl-apcu php70w-mbstring php70w-mysqlnd php70w-mcrypt; yum clean all

RUN sed -i 's/short_open_tag = Off/short_open_tag = On/' /etc/php.ini
