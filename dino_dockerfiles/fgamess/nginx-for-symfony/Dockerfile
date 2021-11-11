FROM nginx

MAINTAINER Franck GAMESS <xxxxxxx@xxxx.com>

RUN apt-get update && apt-get install -y \
    vim

ADD nginx.conf /etc/nginx/
RUN mkdir /etc/nginx/sites-available
RUN mkdir /etc/nginx/sites-enabled
ADD conf.d/http.conf /etc/nginx/conf.d/
ADD upstream.conf /etc/nginx/sites-available/
RUN rm /etc/nginx/conf.d/default.conf
RUN ln -s /etc/nginx/sites-available/upstream.conf /etc/nginx/sites-enabled/upstream.conf

RUN usermod -u 1000 www-data

EXPOSE 80 443
