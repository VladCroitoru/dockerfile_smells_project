FROM centos:latest
MAINTAINER Lu Yun <livecn@163.com>
RUN yum install -y wget
RUN cd /tmp && rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-2.noarch.rpm
RUN yum install -y nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN yum makecache
RUN ["yum", "-y", "install", "php","php-fpm", "php-mysql","php-gd","libjpeg*","php-imap","php-ldap","php-odbc","php-pear","php-xml","php-xmlrpc","php-mbstring","php-mcrypt","php-bcmath","php-mhash","libmcrypt"]
RUN echo "<?php phpinfo(); ?>" > /usr/share/nginx/html/info.php && chown -R nginx:nginx /usr/share/nginx/html/info.php
RUN yum -y install phpmyadmin
RUN ln -s /usr/share/phpMyAdmin /usr/share/nginx/html
RUN [ -e /var/lib/php/session ] || mkdir /var/lib/php/session && chmod -R 0777 /var/lib/php/session
ADD nginx.conf /etc/nginx/conf.d/default.conf
ADD php.ini /etc/php.ini
ADD init.sh /init.sh
ADD config.inc.php /etc/phpMyAdmin/config.inc.php
RUN chmod -R 0755 /etc/phpMyAdmin/config.inc.php
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx","/usr/share/nginx/html"]
WORKDIR /usr/share/nginx/html
RUN chmod a+x /init.sh
CMD ["/init.sh"]
EXPOSE 80
EXPOSE 443
#ENTRYPOINT ["/init.sh"]
