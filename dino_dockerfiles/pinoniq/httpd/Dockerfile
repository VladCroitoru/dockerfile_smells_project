FROM httpd:2.4-alpine

LABEL com.example.vendor="pinoniq" \
      version="1.4"

MAINTAINER Jeroen "pinoniq" Meeus

ARG hostname

RUN mkdir -p /var/www

COPY ./conf/httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./conf/extra/httpd-default.conf /usr/local/apache2/conf/extra/httpd-default.conf
COPY ./conf/extra/httpd-mpm.conf /usr/local/apache2/conf/extra/httpd-mpm.conf
COPY ./entrypoint/httpd-setup.sh /var/scripts/httpd-setup.sh
RUN chmod a+x /var/scripts/httpd-setup.sh

WORKDIR /var/www

ENTRYPOINT ["/var/scripts/httpd-setup.sh"]
