# Reverse proxy container to be used with a static configuration file location
# Config location is mounted at /proxy
FROM nginx

MAINTAINER Adam Pyle <admpyle@gmail.com>

#VOLUME /proxy
RUN mkdir -p /proxy/logs /proxy/config && touch /proxy/logs/access.log /proxy/logs/error.log
# ENV variables/ can be overridden
ENV LOG_DIR=/proxy/logs
ENV ERR_LOG_TYPE=warn

# Remove any default configuration
RUN rm /etc/nginx/conf.d/*.conf
RUN rm /etc/nginx/nginx.conf
ADD nginx/nginx.conf /etc/nginx/
ADD nginx/default.conf /etc/nginx/conf.d/
WORKDIR /usr/src
ADD start.sh /usr/src
RUN chmod 775 start.sh
EXPOSE 80 443

WORKDIR /usr/src

ENTRYPOINT ./start.sh
