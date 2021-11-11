FROM ruby:2.2.2

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list

ENV NGINX_VERSION 1.9.4-1~jessie

RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    ca-certificates \
    nginx=${NGINX_VERSION} \
    node && \
  rm -rf /var/lib/apt/lists/*

RUN gem install pygments.rb jekyll --no-rdoc --no-ri

RUN mkdir /srv/www

WORKDIR /srv/www

ADD default /etc/nginx/conf.d/default.conf
ADD nginx.conf /etc/nginx/nginx.conf

CMD ["nginx"]
