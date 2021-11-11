FROM ubuntu:15.04
MAINTAINER Bradley Bossard <bradleybossard@gmail.com>
 
# install nginx
RUN apt-get update --fix-missing
RUN apt-get -y install wget nginx php5-fpm php5-mysql php5-mongo
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
 
RUN sed -i s/\;cgi\.fix_pathinfo\s*\=\s*1/cgi.fix_pathinfo\=0/ /etc/php5/fpm/php.ini
 
# prepare php test scripts
RUN echo "<?php phpinfo(); ?>" > /usr/share/nginx/html/info.php

# Install latest adminer script and it's css
RUN wget http://www.adminer.org/latest.php -O /usr/share/nginx/html/index.php && \
    wget https://raw.github.com/vrana/adminer/master/designs/hever/adminer.css -O usr/share/nginx/html/adminer.css

RUN mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
COPY default /etc/nginx/sites-available/default
 
# add volumes for debug and file manipulation
#VOLUME ["/var/log/", "/var/www/html/"]
 
EXPOSE 80
 
CMD service php5-fpm start && nginx
