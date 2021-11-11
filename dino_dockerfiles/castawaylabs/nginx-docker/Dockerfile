FROM centos:latest
MAINTAINER Matej Kramny <matej@matej.me>

RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
ADD conf/nginx.repo /etc/yum.repos.d/nginx.repo
RUN yum install -y nginx

EXPOSE 80

ADD www/ /var/www/

RUN rm -rf /etc/nginx/conf.d/*.conf
ADD conf/website.conf /etc/nginx/conf.d/website.conf
ADD conf/nginx.conf /etc/nginx/nginx.conf

ENTRYPOINT ["/usr/sbin/nginx"]
