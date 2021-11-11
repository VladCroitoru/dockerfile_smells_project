FROM mayeco/docker-base

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list

ENV NGINX_VERSION 1.9.3-1~jessie

RUN apt-get update \
    && apt-get install -y --no-install-recommends \ 
        nginx=${NGINX_VERSION} \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD nginx.conf /etc/nginx/
ADD webapp.conf /etc/nginx/sites-enabled/

RUN rm /etc/nginx/conf.d/*
RUN echo "upstream php-upstream { server php:9000; }" > /etc/nginx/conf.d/upstream.conf

WORKDIR /var/www

EXPOSE 80
EXPOSE 443

CMD ["nginx"]
