FROM linuxconfig/lemp
MAINTAINER Daniel Frieling <daniel@frielings.de>

RUN apt-get update
RUN apt-get install -y php-imagick php-ssh2
RUN apt-get clean

RUN sed -i 's/post_max_size = .*/post_max_size = 20M/' /etc/php/7.0/cgi/php.ini
RUN sed -i 's/upload_max_filesize = .*/upload_max_filesize = 20M/' /etc/php/7.0/cgi/php.ini

RUN sed -i '/http {/a  \ \ \ \ \ \ \ \ client_max_body_size 20M; #allow file upload up to that limit' /etc/nginx/nginx.conf

ADD PingPongCockpit/ /var/www/html/

EXPOSE 80 3306

CMD ["supervisord"]
