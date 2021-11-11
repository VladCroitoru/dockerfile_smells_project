# Pull base image.
FROM ubuntu:14.04

MAINTAINER mathieu ledru <matyo91@gmail.com>

# Install default
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade

# Install firefox
RUN apt-get install -y firefox && \
   useradd -s /bin/bash -m -d /home/firefox firefox

# Install ngnix
RUN apt-get install -y nginx

# Install LXDE and VNC server.
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y lxde-core lxterminal tightvncserver

# Copy
COPY html /usr/share/nginx/html
COPY bin/vncserver /usr/local/bin/vncserver
COPY bin/start /usr/local/bin/start
COPY firefox-profile /home/firefox/firefox-profile

EXPOSE 80 5901

CMD ["/usr/local/bin/start"]
