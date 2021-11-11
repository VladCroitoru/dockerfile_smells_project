FROM phusion/baseimage:0.9.16
MAINTAINER Predicsis <francois.cassin@predicsis.com>

ENV HOME /root
ENV LANG en_US.UTF-8
RUN locale-gen en_US.UTF-8

RUN ln -s -f /bin/true /usr/bin/chfn

RUN apt-get update
RUN apt-get -y upgrade

RUN \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0xcbcb082a1bb943db && \
  echo "deb http://mariadb.mirror.iweb.com/repo/10.0/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/mariad\
b.list && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server phpmyadmin wget && \
  rm -rf /var/lib/apt/lists/* && \
  sed -i 's/^\(bind-address\s.*\)/# \1/' /etc/mysql/my.cnf && \
  echo "mysqld_safe &" > /tmp/config && \
  echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \
  echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" WITH GRANT OPTION;'" >> /tmp/config && \
  bash /tmp/config && \
  rm -f /tmp/config

RUN wget -O /usr/local/etc/create_tables.sql https://raw.githubusercontent.com/phpmyadmin/phpmyadmin/master/sql/crea\
te_tables.sql

RUN apt-get update
RUN apt-get -y install \
        ubuntu-cloud-keyring \
        keystone \
        python-keystoneclient \
        python-mysqldb \
        mysql-client \
        memcached \
        python-memcache

RUN apt-get install -y supervisor swift python-swiftclient rsync \
                       swift-proxy swift-object memcached python-keystoneclient \
                       python-swiftclient swift-plugin-s3 python-netifaces \
                       python-xattr python-memcache \
                       swift-account swift-container swift-object pwgen

RUN apt-get -y install \
        openstack-dashboard \
        apache2 \
        libapache2-mod-wsgi \
        memcached \
        python-memcache \
        python-django-nova

RUN apt-get remove -y --auto-remove openstack-dashboard-ubuntu-theme

ADD mariadb/apache2.conf /etc/apache2/apache2.conf
ADD mariadb/config.inc.php /etc/phpmyadmin/config.inc.php
ADD mariadb/initialize_db.sql /root/initialize_db.sql
ADD mariadb/start_apache2.sh /etc/service/apache2/run
ADD mariadb/start_mariadb.sh /etc/service/mariadb/run
ADD initialize.sh /initialize.sh
ADD start.sh /etc/my_init.d/01_start.sh
ADD mariadb/mariadb_config.tar.gz /root/mariadb


ADD keystone/keystone.conf /etc/keystone/keystone.conf
ADD keystone/keystone.tar.gz /root/keystone
#ADD keystone/start_memcached.sh /etc/service/memcached/run
ADD keystone/start_keystone.sh /etc/service/keystone/run


RUN mkdir -p /var/log/supervisor
ADD swift/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ADD swift/dispersion.conf /etc/swift/dispersion.conf
ADD swift/rsyncd.conf /etc/rsyncd.conf
ADD swift/swift.conf /etc/swift/swift.conf
ADD swift/proxy-server.conf /etc/swift/proxy-server.conf
ADD swift/account-server.conf /etc/swift/account-server.conf
ADD swift/object-server.conf /etc/swift/object-server.conf
ADD swift/container-server.conf /etc/swift/container-server.conf
ADD swift/proxy-server.conf /etc/swift/proxy-server.conf
RUN chmod 755 /etc/my_init.d/01_start.sh

ADD horizon/dashboard.py /usr/share/openstack-dashboard/openstack_dashboard/dashboards/project/dashboard.py
ADD horizon/dashboard_admin.py /usr/share/openstack-dashboard/openstack_dashboard/dashboards/admin/dashboard.py

#To add your own logos
#ADD logo-allonge.png /usr/share/openstack-dashboard/static/dashboard/img/logo.png
#ADD logo.png /usr/share/openstack-dashboard/static/dashboard/img/logo-splash.png


ADD horizon/local_settings.py /etc/openstack-dashboard/local_settings.py
ADD horizon/overrides.py /usr/lib/python2.7/overrides.py


ADD horizon/openstack-dashboard.conf /etc/apache2/conf-available/openstack-dashboard.conf
#ADD horizon/start_memcached.sh /etc/service/memcached/run
ADD horizon/start_apache2.sh /etc/service/apache2/run

#django-swiftbrowser

#RUN wget https://bootstrap.pypa.io/get-pip.py
#RUN python get-pip.py
#RUN apt-get install -y python python-pip \
#    && apt-get clean
#RUN pip install django-swiftbrowser
RUN apt-get install -y git
RUN git clone https://github.com/cschwede/django-swiftbrowser.git
ADD swiftbrowser/settings.py /django-swiftbrowser/swiftbrowser/settings.py
ADD swiftbrowser/utils.py /django-swiftbrowser/swiftbrowser/utils.py
ADD swiftbrowser/views.py /django-swiftbrowser/swiftbrowser/views.py
WORKDIR django-swiftbrowser
RUN python setup.py install
ADD swiftbrowser/start_swiftbrowser.sh /etc/service/swiftbrowser/run


EXPOSE 80
EXPOSE 3306
EXPOSE 5000
EXPOSE 35357
EXPOSE 11211
EXPOSE 8080
EXPOSE 8000

RUN /initialize.sh

CMD ["/sbin/my_init"]
