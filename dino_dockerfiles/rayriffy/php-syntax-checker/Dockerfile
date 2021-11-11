FROM centos:centos6.9

MAINTAINER Phumrapee Limpianchop <rayriffy@gmail.com>

RUN yum update -y

RUN yum groupinstall -y 'Development Tools'

RUN yum install -y uglifyjs zip unzip git wget tar gcc gcc+ make nodejs ca-certificates curl sudo

RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm

RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-6.rpm

RUN yum install -y yum-utils

RUN yum-config-manager --enable remi-php70

RUN yum-config-manager --enable remi-php70

RUN yum-config-manager --enable remi-php70

RUN yum install -y php php-curl php-xml php-ldap php-cli php-common php-mysql php-mcrypt php-gd php-zip php-fileinfo php-json

WORKDIR "/root"
