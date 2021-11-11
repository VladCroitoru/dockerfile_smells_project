FROM centos:7

MAINTAINER Vipin Kumar, https://github.com/vipink1203

RUN rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

RUN yum install -y nginx && yum install -y git

RUN rm -rf /usr/share/nginx/html/* && git clone https://github.com/vipink1203/random-quote-machine.git /usr/share/nginx/html/ 

EXPOSE 80

CMD /usr/sbin/nginx -g "daemon off;"
