#
#   Author: Rohith
#   Date: 2015-06-23 15:26:36 +0100 (Tue, 23 Jun 2015)
#
#  vim:ts=2:sw=2:et
#

FROM gambol99/supervisord
MAINTAINER Rohith <gambol99@gmail.com>

ADD config/nginx/nginx.repo /etc/yum.repos.d/nginx.repo

RUN yum install -y --disablerepo=epel --disableplugin=fastestmirror nginx-1.9.2 ruby

ADD config/confd/nginx.toml /etc/confd/conf.d/nginx.toml
ADD config/confd/nginx.conf.tmpl /etc/confd/templates/nginx.conf.tmpl
ADD config/nginx/nginx.conf /etc/nginx/nginx.conf
ADD config/bin/nginx_config /bin/nginx_config
ADD config/bin/nginx_check /bin/nginx_check
ADD config/nginx/nginx.erb /etc/nginx/nginx.erb
ADD config/supervisord/confd.ini /etc/supervisord.d/confd.ini
ADD config/supervisord/nginx.ini /etc/supervisord.d/nginx.ini

RUN chmod +x /bin/nginx_config /bin/nginx_check

ENV ETCD_HOSTS 127.0.0.1:2379

ENTRYPOINT [ "/usr/bin/supervisord", "-n" ]
