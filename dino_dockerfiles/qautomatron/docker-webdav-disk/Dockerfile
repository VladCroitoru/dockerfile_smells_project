FROM phusion/baseimage:0.9.22

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Install rsync and davfs2
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -yqq
RUN apt-get install rsync -yqq
RUN apt-get install davfs2 -yqq

ENV WEBDAV_USER user
ENV WEBDAV_PASSWORD password
ENV WEBDAV_URL http://example.com

# Add starting script
RUN mkdir -p /etc/my_init.d
ADD start.sh /etc/my_init.d/start.sh
RUN chmod +x /etc/my_init.d/start.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
