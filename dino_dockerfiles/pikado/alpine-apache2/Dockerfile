FROM alpine:latest
MAINTAINER Pika Do <pokido99@gmail.com>

# Proxy settings if necessary
# ENV http_proxy=http://proxy:8080
# ENV https_proxy=http://proxy:8080
# ENV no_proxy="127.0.0.1,localhost,.mydomain.com"

# Upgrade system
RUN apk --no-cache upgrade

# Install Apache2 with proxy module
RUN apk --no-cache add apache2 apache2-proxy

# Install various tools
RUN apk --no-cache add curl

# Configure Apache2
RUN mkdir -p /run/apache2 && chown apache: /run/apache2

# Configure proxy module
RUN sed -i 's/^\(LoadModule proxy_balancer.*\)/#\1/g' /etc/apache2/conf.d/proxy.conf

# Define default command
CMD ["httpd","-D","FOREGROUND"]
