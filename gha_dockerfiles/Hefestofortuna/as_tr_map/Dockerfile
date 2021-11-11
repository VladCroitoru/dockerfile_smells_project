FROM centos:8
LABEL version="0.1.3"
RUN yum -y update
RUN dnf install https://rpms.remirepo.net/enterprise/remi-release-8.rpm -y
RUN dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y
RUN mkdir -p /run/php-fpm/
RUN dnf module enable php:remi-8.0 -y
RUN dnf install php php-cli php-common php-pgsql -y
RUN yum install nginx -y
RUN yum install nano -y
RUN yum install dos2unix -y
COPY ./ /app/
COPY ./vagrant/nginx/nginx.conf /etc/nginx/
COPY ./vagrant/php/www.conf /etc/php-fpm.d/
RUN dos2unix /app/*
ENTRYPOINT [ "/app/entrypoint.sh"]