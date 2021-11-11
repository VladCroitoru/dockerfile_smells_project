From centos
RUN rm -rf /etc/yum.repos.d/*
ADD CentOS-Base.repo /etc/yum.repos.d/
ONBUILD ADD start.sh /root/start.sh
RUN yum clean all
RUN yum install -y iproute openssh-client openssh-server net-tools psmisc httpd
RUN sed -i 's/#ServerName www.example.com:80/ServerName www.example.com:80/g' /etc/httpd/conf/httpd.conf
RUN echo 'haha' > /var/www/html/index.html
EXPOSE 80
EXPOSE 22
