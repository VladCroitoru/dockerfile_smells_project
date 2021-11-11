FROM centos:7

WORKDIR /usr/local

COPY ./Centos-7.repo /etc/yum.repos.d/CentOS-Base.repo
RUN yum install -y wget libpng libjpeg openssl icu libX11 libXext libXrender xorg-x11-fonts-Type1 xorg-x11-fonts-75dpi

RUN rpm -ivh https://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm && yum install -y nginx
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

COPY ./mongodb-org-3.6.repo /etc/yum.repos.d/mongodb-org-3.6.repo
RUN yum install -y mongodb-org-tools-3.6.2
ENV MONGO_URL_IP = 127.0.0.1

RUN wget https://bitbucket.org/wkhtmltopdf/wkhtmltopdf/downloads/wkhtmltox-0.13.0-alpha-7b36694_linux-centos7-amd64.rpm && \
    rpm -Uvh wkhtmltox-0.13.0-alpha-7b36694_linux-centos7-amd64.rpm && rm -f wkhtmltox-0.13.0-alpha-7b36694_linux-centos7-amd64.rpm

RUN wget https://jaist.dl.sourceforge.net/project/leanote-bin/2.6/leanote-linux-amd64-v2.6.bin.tar.gz && \
    tar -xzvf leanote-linux-amd64-v2.6.bin.tar.gz && rm -f leanote-linux-amd64-v2.6.bin.tar.gz
COPY app.conf /usr/local/leanote/conf/app.conf
COPY ./init.sh /usr/local/leanote/bin/init.sh

CMD nginx && bash /usr/local/leanote/bin/run.sh
