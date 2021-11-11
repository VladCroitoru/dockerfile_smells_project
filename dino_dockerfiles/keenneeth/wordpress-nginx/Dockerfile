FROM wyveo/nginx-php-fpm
MAINTAINER keenneeth@mail.asix

ADD scriptnginx.sh /scriptnginx.sh
RUN chmod 700 /scriptnginx.sh

EXPOSE 80

CMD ["/scriptnginx.sh"]
