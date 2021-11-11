FROM debian:jessie

RUN echo deb http://nginx.org/packages/debian/ jessie nginx >> /etc/apt/sources.list
RUN echo deb-src http://nginx.org/packages/debian/ jessie nginx >> /etc/apt/sources.list

RUN apt-get update && apt-get -y --force-yes install nginx

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD sites/mesa /etc/nginx/conf.d/default.conf

EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]





