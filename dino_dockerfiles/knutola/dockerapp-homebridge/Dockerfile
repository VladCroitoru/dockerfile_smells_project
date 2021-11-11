FROM phusion/baseimage:0.9.22
MAINTAINER knutola <jonas@knut-ola.com>


# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Set correct environment variables
ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"

COPY start.sh /root/start.sh

# Install 
COPY install.sh /tmp/
RUN bash /tmp/install.sh


EXPOSE 51826


VOLUME /config

RUN apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY config.json /tmp/sample-config.json

CMD ["/root/start.sh"]