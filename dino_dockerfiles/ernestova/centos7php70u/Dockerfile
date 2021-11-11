FROM centos:latest
MAINTAINER Ernesto Vargas <ernesto_vargas@yahoo.com>

# Install dependencies
RUN yum -y install epel-release; yum clean all
RUN rpm -i https://dl.iuscommunity.org/pub/ius/stable/CentOS/7/x86_64/ius-release-1.0-14.ius.centos7.noarch.rpm
RUN rpm -i http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
RUN yum install -y php70u php70u-fpm php70u-cli php70u-devel php70u-gd \
php70u-intl php70u-process  php70u-common php70u-pecl-mongo php70u-mcrypt php70u-pdo php70u-fpm  \
php70u-mysqlnd php70u-pecl-apcu php70u-xml php70u-mbstring nginx supervisor; yum clean all

COPY files/supervisord.conf /etc/supervisord.conf
COPY files/services.conf /etc/supervisord.d/services.conf
COPY files/nginx.conf /etc/nginx/nginx.conf
COPY files/default.conf /etc/nginx/conf.d/default.conf
COPY files/php.ini /etc/php.ini
COPY files/php-fpm.conf /etc/php-fpm.conf
COPY files/www.conf /etc/php-fpm.d/www.conf
COPY files/start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stdout /var/log/nginx/error.log
RUN ln -sf /dev/stdout /var/log/php-fpm/error.log
RUN ln -sf /dev/stdout /var/log/php-fpm/www-slow.log
RUN ln -sf /dev/stdout /var/log/php-fpm/www-error.log

EXPOSE 80

CMD ["/usr/local/bin/start.sh"]
