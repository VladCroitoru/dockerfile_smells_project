FROM centos:6.8
RUN echo 'include_only=.jp' >>/etc/yum/pluginconf.d/fastestmirror.conf
RUN yum -y update && yum -y reinstall glibc-common && yum clean all && cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
COPY files/etc/sysconfig/i18n /etc/sysconfig/i18n
ENV LANG ja_JP.UTF-8
COPY files/etc/sysconfig/clock /etc/sysconfig/clock
COPY files/etc/sysconfig/keyboard /etc/sysconfig/keyboard

RUN \
  yum -y install http://ftp.riken.jp/Linux/fedora/epel/epel-release-latest-6.noarch.rpm \
  && yum -y install git \
  && yum clean all

RUN \
  yum -y install http://dev.mysql.com/get/mysql57-community-release-el6-9.noarch.rpm \
  && yum --disablerepo=mysql57-community --enablerepo=mysql55-community -y install mysql-community-server \
  && yum clean all
RUN su mysql -c "mysql_install_db"

RUN \
  yum -y install http://rpms.famillecollet.com/enterprise/remi-release-6.rpm \
  && yum -y install --enablerepo=remi,remi-php55 \
  php55-php \
  php55-php-pear \
  php55-php-devel \
  php55-php-xml \
  php55-php-mbstring \
  php55-php-gd \
  php55-php-pgsql \
  php55-php-mysqlnd \
  php55-php-mcrypt \
  php55-php-intl \
  php55-php-opcache \
  php55-php-pdo \
  && yum clean all
COPY files/opt/remi/php55/root/etc/php.d/zzz-my.ini /opt/remi/php55/root/etc/php.d/zzz-my.ini
RUN sed -ri 's/^;opcache\.enable_cli=.*$/opcache.enable_cli=1/' /opt/remi/php55/root/etc/php.d/opcache.ini
COPY files/etc/profile.d/enablephp55.sh /etc/profile.d/enablephp55.sh
RUN chmod 0644 /etc/profile.d/enablephp55.sh

CMD ["/bin/bash"]
