FROM debian:wheezy

MAINTAINER Ozzyboshi "gun101@email.it"

# RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
# RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list

ENV NGINX_VERSION 1.7.14-1~wheezy

RUN apt-get update && apt-get install -y nginx wget ca-certificates && rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

# RUN rm /etc/nginx/conf.d/default.conf
ADD default.conf /etc/nginx/conf.d/

RUN wget https://github.com/Ozzyboshi/GuakeIndicatorWebsite/archive/4.tar.gz
RUN mkdir /guake-indicator && tar -xvzpf 4.tar.gz -C /guake-indicator/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
