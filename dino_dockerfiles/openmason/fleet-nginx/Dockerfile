# Webserver (nginx) image description
#
# Usage:
# docker build -t openmason/fleet-nginx .
#
#
FROM openmason/fleet-base:latest
MAINTAINER el aras<openmason@gmail.com>

# env variables

# ppa repositories
RUN add-apt-repository ppa:nginx/stable

# Install nginx
RUN \
  apt-get update; \
  apt-get install -yq nginx php5-fpm --no-install-recommends; \
  pip install --upgrade circus-web chaussette; \
  apt-get clean

# Remove the default Nginx configuration file
RUN rm -v /etc/nginx/nginx.conf

# copy default config files
ADD nginx/nginx.conf              /etc/nginx/nginx.conf
ADD nginx/sites-enabled           /etc/nginx/sites-enabled
ADD logrotate/nginx               /etc/logrotate.d/nginx
ADD circus/conf.d/nginx.conf      /etc/circus/conf.d/nginx.conf
ADD circus/conf.d/circusweb.conf  /etc/circus/conf.d/circusweb.conf

# add "daemon off;" 
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# mountable directories
#VOLUME ["/var/log/nginx", "/etc/nginx/sites-enabled"]

# Expose ports
EXPOSE 80 443

# Set the default command to execute
# when creating a new container
CMD ["/usr/local/bin/circusd", "/etc/circusd.conf"]
