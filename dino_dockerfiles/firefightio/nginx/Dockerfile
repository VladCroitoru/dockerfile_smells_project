#
# Nginx Dockerfile
#
# https://github.com/firefight.io/nginx
# 

# Pull base image.
FROM ubuntu

# Install Nginx.
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update
RUN apt-get install -y nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

# Attach volumes.
VOLUME /etc/nginx/sites-enabled
VOLUME /var/log/nginx
VOLUME /usr/share/nginx/html/

# Add website files
ADD default /etc/nginx/sites-enabled/default

# Expose ports.
EXPOSE 80

# Define default command.
CMD ["nginx"]
