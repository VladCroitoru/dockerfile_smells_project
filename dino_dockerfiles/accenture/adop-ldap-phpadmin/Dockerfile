FROM alpine:3.3

MAINTAINER Maksym Nebot <maksym.nebot@accenture.com>

ENV LDAP_SERVER_NAME 'ADOP LDAP'
ENV LDAP_SERVER_HOST 'ldap'
ENV LDAP_SERVER_PORT '389'
ENV LDAP_SERVER_BIND_ID 'cn=admin,dc=ldap,dc=example,dc=com'
ENV LDAP_SERVER_BASE_DN 'dc=ldap,dc=example,dc=com'

RUN apk update \
    && apk add bash nginx ca-certificates \
    php-fpm php-json php-zlib php-xml php-pdo php-phar php-openssl \
    php-pdo_mysql php-mysqli \
    php-gd php-iconv php-mcrypt php-ldap phpldapadmin

# fix php-fpm "Error relocating /usr/bin/php-fpm: __flt_rounds: symbol not found" bug
RUN apk add -u musl
RUN rm -rf /var/cache/apk/*

WORKDIR ["/usr/share/webapps/phpldapadmin/htdocs"]

ADD files/config.php  /usr/share/webapps/phpldapadmin/config/
ADD files/nginx.conf /etc/nginx/
ADD files/php-fpm.conf /etc/php/

ADD files/run.sh /
RUN chmod +x /run.sh

EXPOSE 80

CMD ["/run.sh"]
