FROM giabar/gb-httpd-centos
LABEL maintainer="giabar@giabar.com"
ENV DOWNLOAD_URL https://github.com/LimeSurvey/LimeSurvey/archive/3.8.2+180529.tar.gz
RUN yum clean all &&\
    rm -rf /var/tmp/ &&\
    rm -rf /var/cache/yum &&\
    yum -y install php-imap wget tar &&\
    wget $DOWNLOAD_URL &&\
    tar zxvf 3.8.2+180529.tar.gz &&\
    rm -f 3.8.2+180529.tar.gz &&\
    mv limesurvey/* /var/www/html/ &&\
    rm -rf limesurvey/ &&\
    chmod -R 775 /var/www/html/ &&\
    chmod -R 777 /var/www/html/tmp/ &&\
    chmod -R 777 /var/www/html/upload/ &&\
    chmod -R 777 /var/www/html/application/config/ &&\
    yum clean all &&\
    rm -rf /var/tmp/ &&\
    rm -rf /var/cache/yum
VOLUME /var/www/html
EXPOSE 80 443
