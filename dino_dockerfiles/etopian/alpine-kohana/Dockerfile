FROM alpine:edge
MAINTAINER Etopian Inc. <contact@etopian.com>

LABEL   devoply.type="site" \
        devoply.cms="kohana" \
        devoply.framework="kohana" \
        devoply.language="php" \
        devoply.require="mariadb etopian/nginx-proxy" \
        devoply.recommend="redis" \
        devoply.description="Kohana on Nginx and PHP-FPM." \
        devoply.name="Kohana" \
        devoply.params="docker run -d --name {container_name} -e VIRTUAL_HOST={virtual_hosts} -v /data/sites/{domain_name}:/DATA etopian/alpine-kohana"


RUN apk update \
    && apk add bash less vim nginx ca-certificates \
    php-fpm php-json php-zlib php-xml php-pdo php-phar php-openssl \
    php-pdo_mysql php-mysqli \
    php-gd php-iconv php-mcrypt postfix \
    php-mysql php-curl php-opcache php-ctype php-apcu \
    php-intl php-bcmath php-dom php-xmlreader mysql-client && \
    apk add -u musl

RUN rm -rf /var/cache/apk/*

# configure postfix use to amazon ses to send mail.
ENV SES_HOST="email-smtp.us-east-1.amazonaws.com" SES_PORT="587" \
    SES_USER="" SES_SECRET="" TERM="xterm" \
    DB_HOST="172.17.42.1" DB_USER="" DB_PASS="" DB_NAME=""


RUN sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php/php.ini
ADD files/nginx.conf /etc/nginx/
ADD files/php-fpm.conf /etc/php/
ADD files/run.sh /
RUN chmod +x /run.sh
ADD files/postfix/setup_ses.sh /setup_ses.sh
RUN chmod +x /setup_ses.sh && /setup_ses.sh
ADD files/postfix/main.cf /etc/postfix/main.cf


EXPOSE 80
VOLUME ["/DATA"]

CMD ["/run.sh"]
