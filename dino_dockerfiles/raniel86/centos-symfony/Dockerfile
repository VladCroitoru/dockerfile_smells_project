FROM centos:latest

# PHP 5.6
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm
RUN yum install -y yum-utils
RUN yum-config-manager --enable remi-php56
RUN yum install -y php php-mcrypt php-cli php-gd php-curl php-mysql php-ldap php-zip php-fileinfo php-xml php-soap php-pgsql php-devel php-pdo php-mysqlnd php-opcache php-common php-mbstring php-process php-pear php-fpm php-pecl-memcache php-pecl-jsonc php-pecl-jsonc-devel php-pecl-apcu
RUN sed -ie 's/;date\.timezone =/date\.timezone = Europe\/Rome/g' /etc/php.ini

# MySQL
RUN yum install -y mysql mysql-server

# nodejs
RUN yum install -y nodejs npm

# ant ansible
RUN yum install -y ant ansible

# Other packages
RUN yum install -y wget zip

# composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/bin/composer
