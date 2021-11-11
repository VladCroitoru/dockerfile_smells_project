FROM debian:jessie
MAINTAINER Alessandro Poli <alessandro.poli@protonmail.ch>
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
    && echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
                        ca-certificates \
                        nginx \
                        gettext-base \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /static-app
COPY default.conf /etc/nginx/conf.d/
WORKDIR /static-app
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
