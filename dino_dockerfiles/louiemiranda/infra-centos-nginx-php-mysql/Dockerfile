#
# infra-centos-nginx-php-mysql
#
FROM centos:6
MAINTAINER Louie Miranda <lmiranda@gmail.com>

#
# INSTALLATION ###########################################
#

RUN yum -y install epel-release
RUN yum -y install wget
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
RUN wget https://centos6.iuscommunity.org/ius-release.rpm

#
# MYSQL
#
RUN wget http://repo.mysql.com/mysql-community-release-el6-5.noarch.rpm
RUN rpm -ivh mysql-community-release-el6-5.noarch.rpm

RUN rpm -Uvh ius-release*.rpm
RUN yum -y update

#
# Installing web application components
#
RUN yum -y install php56u-fpm php56u php56u-opcache php56u-xml php56u-mcrypt php56u-gd php56u-devel php56u-mysql php56u-intl php56u-mbstring php56u-bcmath php56u-pecl-memcache php56u-pecl-memcached
RUN yum -y install mysql-server mysql-client
RUN yum -y install memcached

#
# Installing other utilities
#
RUN yum -y install git software-properties-common zip unzip vim gcc

#
# Installing nginx from package
#
RUN yum -y install nginx

#
# Installing nginx from source with add more headers
#
ADD scripts/ /tmp/scripts
RUN ["sh","/tmp/scripts/install_nginx_header.sh"]
ADD  settings/nginx/nginx.conf /etc/nginx/nginx.conf

#
# Installing Phalcon 2.0.13
#
RUN git clone -b 2.0.x https://github.com/phalcon/cphalcon.git cphalcon && \
    cd cphalcon/build/ && \
    ./install && \
    cd /tmp && \
    /bin/rm -rfv /tmp/cphalcon/

RUN /bin/echo 'extension=phalcon.so' > /etc/php.d/phalcon.ini

#
# Install Composer and make it available in the PATH
#
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

# AWS
RUN yum install -y centos-release-scl scl-utils scl-utils-build && \
    yum --disablerepo='*' \
    --enablerepo='centos-sclo-rh' \
    install -y python27
RUN scl enable python27 'python -V' && \
    source scl_source enable python27 && \
    curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
    unzip awscli-bundle.zip && \
    ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

# XML PARSER
RUN pear install XML_Parser

# SUPERVISORD
RUN yum -y install supervisor
RUN chkconfig supervisord on

# PHPUNIT
RUN composer global require "phpunit/phpunit" && ln -s /root/.composer/vendor/bin/phpunit /usr/bin/phpunit