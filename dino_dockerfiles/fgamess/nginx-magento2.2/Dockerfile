FROM nginx

MAINTAINER Franck GAMESS <xxxxxxx@gmail.com>

ADD nginx.conf /etc/nginx/
ADD nginx.conf.sample /etc/nginx/
RUN mkdir /etc/nginx/sites-available
ADD magento /etc/nginx/sites-available/

RUN rm /etc/nginx/conf.d/default.conf

ARG NGINX_HOST_ARG
ENV NGINX_HOST $NGINX_HOST_ARG
RUN envsubst '${NGINX_HOST}' < /etc/nginx/sites-available/magento > /etc/nginx/sites-available/magento

#RUN echo "upstream php-upstream { server php:9000; }" > /etc/nginx/conf.d/upstream.conf

RUN usermod -u 1000 www-data

CMD ["nginx"]

EXPOSE 80
EXPOSE 443
