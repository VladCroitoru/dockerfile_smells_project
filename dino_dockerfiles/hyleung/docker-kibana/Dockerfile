FROM nginx
MAINTAINER H.Y. Leung <hy.leung@gmail.com>

RUN apt-get -yqq update
RUN apt-get -yqq install wget

RUN mkdir -p /var/www
WORKDIR /var/www
RUN wget http://download.elasticsearch.org/kibana/kibana/kibana-3.1.2.tar.gz -O kibana.tar.gz
RUN tar -xzvf kibana.tar.gz
RUN mv kibana-3.1.2 kibana
RUN rm kibana.tar.gz 

VOLUME /var/www/kibana

ADD files/kibana.config.js /var/www/kibana/config.js
ADD files/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8888
