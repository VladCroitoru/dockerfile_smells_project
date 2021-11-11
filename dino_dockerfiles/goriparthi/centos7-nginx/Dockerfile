#Author:PG - Demo/Training/Testing

FROM centos:centos7

RUN yum -y update --nogpgcheck; yum clean all

#Install nginx repo
RUN rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

# Install latest version of nginx
RUN yum install -y nginx --nogpgcheck

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

#Install required php 5.6 packages
RUN yum install -y php php-fpm --nogpgcheck

#Update PHP configs
ADD ./php.ini /etc/php.ini
ADD ./www.conf /etc/php-fpm.d/www.conf

#Update nginx config
ADD ./default.conf /etc/nginx/conf.d/default.conf

ADD ./index.php /usr/share/nginx/html/index.php

# Install supervisor to run jobs
RUN yum install -y epel-release --nogpgcheck
RUN yum install -y supervisor --nogpgcheck

ADD ./supervisord.conf /etc/supervisord.conf

EXPOSE 80
EXPOSE 443

#Run nginx engine
CMD ["/usr/bin/supervisord","-n","-c","/etc/supervisord.conf"]
