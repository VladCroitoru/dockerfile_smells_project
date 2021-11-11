FROM haproxy:1.7
MAINTAINER Jonni Rainisto <jonni.rainisto@gmail.com>

# Create a system group and user to be used by HAProxy.
RUN groupadd haproxy && useradd -g haproxy haproxy && mkdir /var/lib/haproxy

# Define working directory.
WORKDIR /etc/haproxy

# Add personalized configuration
ADD haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

VOLUME /certs:/certs

# Expose ports.
EXPOSE 80
EXPOSE 443
EXPOSE 1883
EXPOSE 18083
