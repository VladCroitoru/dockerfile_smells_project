#
# INFRA-CENTOS6-PHP56-NGINX-MYSQL-CPHALCON Docker/Codeship CentOS with Web Application Components
#
FROM centos:6
MAINTAINER Louie Miranda <lmiranda@gmail.com>

RUN yum -y install epel-release
RUN yum -y install wget
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
RUN wget https://centos6.iuscommunity.org/ius-release.rpm

# MYSQL
RUN wget http://repo.mysql.com/mysql-community-release-el6-5.noarch.rpm
RUN rpm -ivh mysql-community-release-el6-5.noarch.rpm

RUN rpm -Uvh ius-release*.rpm
RUN yum -y update

# Installing web application components
RUN yum -y install php56u-fpm php56u php56u-opcache php56u-xml php56u-mcrypt php56u-gd php56u-devel php56u-mysql php56u-intl php56u-mbstring php56u-bcmath php56u-pecl-memcache php56u-pecl-memcached

# Installing mysql
RUN yum -y install mysql-server mysql-client


# Installing memcached
RUN yum -y install memcached

# Installing compiler, git 
RUN yum -y install git gcc

# Installing tools
RUN yum -y install vim

# Installing nginx 
RUN yum -y install nginx

# Installing nginx from source with add more headers
# RUN pwd
ADD scripts/ /tmp/scripts

RUN ls -la /tmp/scripts/
RUN ["sh","/tmp/scripts/install_nginx_header.sh"]

# COPY scripts/init.sh /etc/init.d

#
# Installing Phalcon 2.0.13
#
RUN git clone -b 2.0.x https://github.com/phalcon/cphalcon.git cphalcon && \
    cd cphalcon/build/ && \
    ./install && \
    cd /tmp && \
    /bin/rm -rfv /tmp/cphalcon/

RUN /bin/echo 'extension=phalcon.so' > /etc/php.d/phalcon.ini

# Installing other utilities
RUN yum -y install git software-properties-common zip unzip

# Install Composer and make it available in the PATH
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

# Other configs / timezone, short tags, etc
#COPY settings/php.d /etc/php.d

# Adding the configuration file of the nginx
#COPY settings/nginx/conf.d /etc/nginx/conf.d
ADD  settings/nginx/nginx.conf /etc/nginx/nginx.conf

#CMD ["sh","scripts/start.sh"]