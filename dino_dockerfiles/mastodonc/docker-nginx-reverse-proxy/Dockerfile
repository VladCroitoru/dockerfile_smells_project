#
# Nginx Dockerfile
#

# Pull base image.
FROM ubuntu:14.04

# Install Nginx.
RUN \
  apt-get update && \
  apt-get install -y software-properties-common python-software-properties && \
  add-apt-repository -y ppa:nginx/stable && \
  apt-get update && \
  apt-get install -y nginx && \
  rm -rf /var/lib/apt/lists/* && \
  echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
  chown -R www-data:www-data /var/lib/nginx

# Define working directory.
WORKDIR /etc/nginx

ADD start-nginx.sh /start-nginx

# Define default command.
CMD ["/bin/bash","/start-nginx"]

# Expose ports.
EXPOSE 80
EXPOSE 443
