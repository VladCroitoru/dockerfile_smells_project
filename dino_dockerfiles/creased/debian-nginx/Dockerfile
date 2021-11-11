#
# Nginx Dockerfile
#
# Written by:
#   Baptiste MOINE <contact@bmoine.fr>
#

# Pull base image (ie, Debian 8).
FROM debian:8

MAINTAINER Baptiste MOINE <contact@bmoine.fr>

# Non-interactive frontend.
ENV DEBIAN_FRONTEND noninteractive

# Copy sourcelist for APT.
COPY ./files/apt/sources.list /etc/apt/sources.list

# Note: Each RUN instruction will perform a commit of the image.
# Install Nginx and PHP using only one instruction.
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys ABF5BD827BD9BF62 \
&& apt-get update \
&& apt-get install -y --no-install-recommends --no-install-suggests \
                   ca-certificates \
                   nginx="1.9.0-1~jessie" \
                   spawn-fcgi \
                   gettext-base \
                   php5-fpm \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Create Nginx and PHP file structure.
RUN rm -rf /usr/share/nginx/html/ \
&& mkdir -p /etc/nginx.default/conf.d/ \
&& mkdir -p /etc/php5/fpm.default/pool.d/ \
&& mkdir -p /usr/share/nginx/log \
&& mkdir -p /usr/share/nginx/static \
&& mkdir -p /usr/share/nginx/webroot \
&& touch /usr/share/nginx/log/access.log \
&& touch /usr/share/nginx/log/error.log \
&& rm /etc/nginx/nginx.conf \
&& rm /etc/php5/fpm/pool.d/www.conf

# Copy default Nginx configuration files using ADD to keep directory structure (issue #15858).
ADD ./files/nginx/conf/ /etc/nginx.default/

# Copy default PHP configuration files using ADD to keep directory structure (issue #15858).
ADD ./files/fpm/conf/ /etc/php5/fpm.default/

# Add default webroot using ADD to keep directory structure (issue #15858).
ADD ./files/nginx/webroot/ /usr/share/nginx/webroot/

# Copy Startup script.
COPY ./files/start.sh /start.sh
RUN chmod u+x /start.sh

# Create volumes.
VOLUME ["/etc/nginx/", "/etc/php5/fpm/", "/usr/share/nginx/", "/var/www/"]

# TCP port that container will listen for connections.
# HTTP and HTTPS.
EXPOSE 80/tcp 443/tcp

# Alternative to: CMD ["nginx", "-g", "daemon off;"]
CMD ["/start.sh"]

