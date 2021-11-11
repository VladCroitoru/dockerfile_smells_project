FROM senbazuru/docker-php56
MAINTAINER senbazuru

RUN yum install -y --enablerepo=remi-php56,remi \
php-pecl-mongo \
php-pecl-runkit \
php-pecl-imagick \
php-pecl-memcache \
php-pecl-memcached 
RUN yum clean all

