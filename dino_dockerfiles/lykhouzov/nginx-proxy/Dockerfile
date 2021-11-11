FROM centos:7

MAINTAINER Aleksandr Lykhouzov <lykhouzov@gmail.com>

RUN echo $'[nginx]\n\
name=nginx repo\n\
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/\n\
gpgcheck=0\n\
enabled=1\n\
' | tee /etc/yum.repos.d/nginx.repo;\
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
# Install NGINX
&& yum -y update && yum install -y \
nginx luajit lua \
&& /usr/bin/yum clean all \
&& rm -f /etc/nginx/conf.d/*

EXPOSE 80 443
CMD ["nginx","-g","daemon off;"]
