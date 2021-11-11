#
# Cobbler Dockerfile
#
# https://github.com/iilab/docker-cobbler
#

# Pull base image.
FROM dockerfile/ubuntu

RUN apt-get update
RUN apt-get install -y python-zope.interface
RUN apt-get install -y python-twisted
RUN apt-get install -y apache2

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q tftpd-hpa

#ENV DEBIAN_FRONTEND noninteractive

# Install Cobbler.
RUN apt-get install -y cobbler cobbler-web
#  cobbler check && \
#  cobbler sync

# Define mountable directories.
#VOLUME ["/data", "/etc/nginx/sites-enabled", "/var/log/nginx"]

# Define working directory.
#WORKDIR /etc/nginx

# Define default command.
#CMD ["nginx"]

# Expose ports.
EXPOSE 80
EXPOSE 443
