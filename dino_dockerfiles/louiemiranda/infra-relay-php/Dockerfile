#
# INFRA-RELAY-PHP CentOS with Web Application Components on Codeship
#
FROM centos:6
MAINTAINER Louie Miranda <lmiranda@gmail.com>

WORKDIR /tmp

RUN yum -y install epel-release
RUN yum -y install wget
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
RUN wget https://centos6.iuscommunity.org/ius-release.rpm
RUN rpm -Uvh ius-release*.rpm
RUN yum -y update

# Installing web application components
RUN yum -y install php56u-fpm php56u php56u-opcache php56u-xml php56u-mcrypt php56u-gd php56u-devel php56u-mysql php56u-intl php56u-mbstring php56u-bcmath php56u-pecl-memcache

# Installing mysql
# RUN yum -y install mysql-server mysql-client

# Install MariaDB
# RUN echo -e "[mariadb]" >> /etc/yum.repos.d/MariaDB.repo && \
#     echo -e "name = MariaDB" >> /etc/yum.repos.d/MariaDB.repo && \
#     echo -e "baseurl = http://yum.mariadb.org/10.0/centos6-amd64" >> /etc/yum.repos.d/MariaDB.repo && \
#     echo -e "gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB" >> /etc/yum.repos.d/MariaDB.repo && \
#     echo -e "gpgcheck=1" >> /etc/yum.repos.d/MariaDB.repo && \
#     yum -y install MariaDB-Galera-server MariaDB-client galera

# INSTALL WEB ESSENTIALS

## Installing nginx 
RUN yum -y install nginx

## Installing git
RUN yum -y install git

## Installing other utilities
RUN yum -y install git software-properties-common zip unzip

# Install Composer and make it available in the PATH
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

# Install Automation Tools
RUN yum -y install ansible

RUN curl -SLO "https://s3.amazonaws.com/codeship-jet-releases/1.19.3/jet-linux_amd64_1.19.3.tar.gz"

RUN tar -xaC /usr/local/bin -f jet-linux_amd64_1.19.3.tar.gz

RUN chmod +x /usr/local/bin/jet

RUN wget http://stedolan.github.io/jq/download/linux64/jq

RUN chmod +x ./jq

RUN cp jq /usr/bin

# Misc
RUN pear install XML_Parser

RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
    unzip awscli-bundle.zip && \
    ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

RUN echo -e "date.timezone=\"Asia/Singapore\"" > /etc/php.d/timezone.ini