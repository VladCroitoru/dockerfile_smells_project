FROM centos:6.7
MAINTAINER sadapon2008 <sadapon2008@gmail.com>

RUN echo -n 'root:root' | chpasswd

RUN echo 'include_only=.jp' >>/etc/yum/pluginconf.d/fastestmirror.conf

RUN yum -y update && yum clean all

RUN yum -y reinstall glibc-common && yum clean all

RUN echo 'LANG="ja_JP.UTF-8"' >/etc/sysconfig/i18n

ENV LANG ja_JP.UTF-8

RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN echo 'ZONE="Asia/Tokyo"' >/etc/sysconfig/clock

RUN echo 'KEYTABLE="jp106"' >/etc/sysconfig/keyboard
RUN echo 'MODEL="jp106"' >>/etc/sysconfig/keyboard
RUN echo 'LAYOUT="jp"' >>/etc/sysconfig/keyboard
RUN echo 'KEYBOARDTYPE="pc"' >>/etc/sysconfig/keyboard

RUN yum -y install openssh-server openssh-clients
RUN sed -ri 's/^#AddressFamily any/AddressFamily inet/' /etc/ssh/sshd_config
RUN sed -ri 's/^#UseDNS yes/UseDNS no/' /etc/ssh/sshd_config
RUN sed -ri 's/^GSSAPIAuthentication yes/GSSAPIAuthentication no/' /etc/ssh/sshd_config
RUN chkconfig sshd on

RUN yum -y install http://ftp.riken.jp/Linux/fedora/epel/epel-release-latest-6.noarch.rpm && yum clean all

RUN yum -y install git && yum clean all

RUN yum -y install http://yum.postgresql.org/9.5/redhat/rhel-6.7-x86_64/pgdg-centos95-9.5-2.noarch.rpm && yum clean all
RUN yum -y install postgresql95-server postgresql95-contrib && yum clean all
RUN su postgres -c "/usr/pgsql-9.5/bin/initdb --no-locale --encoding=UTF8 -D /var/lib/pgsql/9.5/data"
RUN chkconfig postgresql-9.5 on

RUN yum -y install http://rpms.famillecollet.com/enterprise/remi-release-6.rpm && yum clean all
RUN yum -y install \
  php56-php \
  php56-php-pear \
  php56-php-devel \
  php56-php-xml \
  php56-php-mbstring \
  php56-php-gd \
  php56-php-pgsql \
  php56-php-mysqlnd \
  php56-php-mcrypt \
  php56-php-intl \
  php56-php-opcache \
  php56-php-pdo
RUN echo '[global]' >/opt/remi/php56/root/etc/php.d/99-my.ini
RUN echo 'expose_php = Off' >>/opt/remi/php56/root/etc/php.d/99-my.ini
RUN echo 'memory_limit = 256M' >>/opt/remi/php56/root/etc/php.d/99-my.ini
RUN echo 'short_open_tag = Off' >>/opt/remi/php56/root/etc/php.d/99-my.ini
RUN echo '' >>/opt/remi/php56/root/etc/php.d/99-my.ini
RUN echo '[mbstring]' >>/opt/remi/php56/root/etc/php.d/99-my.ini
RUN echo 'mbstring.language = Japanese' >>/opt/remi/php56/root/etc/php.d/99-my.ini
RUN echo 'mbstring.internal_encoding = utf-8' >>/opt/remi/php56/root/etc/php.d/99-my.ini
RUN echo '' >>/opt/remi/php56/root/etc/php.d/99-my.ini
RUN echo '[Date]' >>/opt/remi/php56/root/etc/php.d/99-my.ini
RUN echo 'date.timezone = Asia/Tokyo' >>/opt/remi/php56/root/etc/php.d/99-my.ini
RUN sed -ri 's/^;opcache\.enable_cli=.*$/opcache.enable_cli=1/' /opt/remi/php56/root/etc/php.d/10-opcache.ini
RUN echo '#!/bin/bash' >/etc/profile.d/enablephp56.sh
RUN echo 'source /opt/remi/php56/enable' >>/etc/profile.d/enablephp56.sh
RUN echo 'export X_SCLS="`scl enable php56 'echo $X_SCLS'`"' >>/etc/profile.d/enablephp56.sh
RUN chmod 0644 /etc/profile.d/enablephp56.sh

EXPOSE 22

CMD ["/sbin/init"]
