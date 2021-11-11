FROM alpine:latest
MAINTAINER Pika Do <pokido99@gmail.com>

# Settings Proxy if necessary
#ENV http_proxy http://proxy..mydomain.comc:8080
#ENV https_proxy http://proxyva..mydomain.com:8080
#ENV no_proxy 127.0.0.1,localhost,.mydomain.com

# Upgrade system
RUN apk --no-cache upgrade

# Install nginx
RUN apk --no-cache add nginx

# Set default command
EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]