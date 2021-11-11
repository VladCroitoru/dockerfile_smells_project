FROM debian:jessie

MAINTAINER "Dylan Miles" <dylan.g.miles@gmail.com>

WORKDIR /tmp

# Install Nginx
RUN apt-get update -y && \
    apt-get install -y nginx

# Apply Nginx configuration
ADD config/nginx.conf /opt/etc/nginx.conf
ADD config/moodle /etc/nginx/sites-available/moodle
RUN ln -s /etc/nginx/sites-available/moodle /etc/nginx/sites-enabled/moodle && \
    rm /etc/nginx/sites-enabled/default

# Nginx startup script
ADD config/nginx-start.sh /opt/bin/nginx-start.sh
RUN chmod u=rwx /opt/bin/nginx-start.sh

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /data
VOLUME ["/data"]

# PORTS
EXPOSE 80
EXPOSE 443

WORKDIR /opt/bin
ENTRYPOINT ["/opt/bin/nginx-start.sh"]
