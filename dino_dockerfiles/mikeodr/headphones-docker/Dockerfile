FROM phusion/baseimage:0.9.17
MAINTAINER Specter <mike@mikeodriscoll.ca>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root

CMD ["/sbin/my_init"]

RUN usermod -u 99 nobody
RUN usermod -g 100 nobody

RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe multiverse"
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse"
RUN apt-get update -qq
RUN apt-get upgrade -qq

# Install Dependencies
RUN apt-get install -qq -y git python python-cheetah ca-certificates


# Install Headphones
RUN mkdir /opt/headphones
RUN git clone https://github.com/rembo10/headphones.git -b master /opt/headphones
RUN chown -R nobody:users /opt/headphones

EXPOSE 8181

# Headphones Configuration
VOLUME /config

# Downloads
VOLUME /downloads

# TV directory
VOLUME /music

ADD config/config.ini /root/config.ini

# Add Headphones to runit
RUN mkdir /etc/service/headphones
ADD init/headphones.sh /etc/service/headphones/run
RUN chmod +x /etc/service/headphones/run
