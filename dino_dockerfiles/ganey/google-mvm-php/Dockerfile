# DOCKER-VERSION 1.0.0
FROM centos:centos6.7

# Install repos
RUN yum update -y >/dev/null; yum install -y http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm; yum install -y http://dl.fedoraproject.org/pub/epel/6/x86_64/supervisor-2.1-9.el6.noarch.rpm; rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm

#install nginx, php, opcache, git, nano, vim, memcached, supervisor
RUN ["yum", "-y", "install", "nginx", "php56w", "php56w-common", "php56w-fpm", "php56w-mcrypt", "php56w-mbstring", "php56w-curl", "php56w-mysql", "php56w-sqlite", "php56w-pdo", "php56w-devel", "php56w-gd", "php56w-pecl-memcached", "php56w-pecl-memcache", "php56w-pspell", "php56w-snmp", "php56w-xmlrpc", "php56w-xml", "php-opcache", "git", "nano", "vim", "memcached", "supervisor"]

#fix nano
RUN echo "export TERM=xterm" >> /root/.bashrc

# Create folder for server and add index.php file to for nginx
RUN mkdir -p /var/www/public && chmod a+r /var/www/public && echo "<?php phpinfo(); ?>" > /var/www/public/index.php

# nginx config, supervisor config, memcached, php settings
COPY docker /etc/

EXPOSE 8080

# Add working dir to /var/www
#ADD . /var/www

# Fix dir perms
RUN chown -Rf apache:apache /var/www && chown -R nobody:nobody /var/lib/nginx/tmp && chmod -R 755 /var/lib/nginx/tmp

# Executing supervisord
CMD ["supervisord", "-n"]

# build this docker
# sudo docker build -t=ganey/google-mvm-php .

# run this docker
# sudo docker run --name=gvm -v /e/websites/website-name:/var/www -p 8080:8080 ganey/google-mvm-php