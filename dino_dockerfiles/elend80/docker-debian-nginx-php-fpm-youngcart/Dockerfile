FROM elend80/docker-debian-nginx-php-fpm:latest
MAINTAINER "Youngho Byun (echoes)" <elend80@gmail.com>

ENV TERM xterm

RUN echo Asia/Seoul | tee /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get update
RUN apt-get install -y php5-mysql php5-gd php5-cgi curl php5-curl php5-json php-soap openssl

ADD nginx.conf /etc/nginx/nginx.conf

ADD default.conf /etc/nginx/conf.d/default.conf

RUN adduser www-data www-data

RUN mkdir /var/www
RUN cp /usr/share/nginx/html/50x.html /var/www/50x.html
RUN rm -rf /usr/share/nginx/html

# Youngcart

RUN git clone --branch master https://github.com/gnuboard/youngcart5.git /tmp/youngcart5 && \
    mv /tmp/youngcart5/* /var/www/ && \
    rm -rf tmp/youngcart5 && \
    chown -R www-data:www-data /var/www && \
    mkdir /var/www/data && chmod 0707 -R /var/www/data


EXPOSE 80
EXPOSE 443

CMD ["/usr/bin/supervisord"]
