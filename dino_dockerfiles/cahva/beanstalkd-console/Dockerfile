FROM php:5.6
MAINTAINER Markku Virtanen <cahva@po-rno.fi>

ADD install.sh install.sh
ADD replaceauth.sh replaceauth.sh
RUN docker-php-ext-install mbstring
RUN chmod +x install.sh && chmod +x replaceauth.sh && sleep 1 && ./install.sh && rm install.sh

EXPOSE 2080
CMD ./replaceauth.sh && bash -c 'BEANSTALK_SERVERS=$BEANSTALKD_PORT_11300_TCP_ADDR:11300 php -S 0.0.0.0:2080 -t /source/public'
