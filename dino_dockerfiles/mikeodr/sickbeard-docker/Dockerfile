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
RUN apt-get install -qq -y git python python-cheetah ca-certificates wget unrar unzip


# Install SickBeard
RUN mkdir /opt/sickbeard
RUN git clone https://github.com/midgetspy/Sick-Beard.git -b master /opt/sickbeard
RUN chown -R nobody:users /opt/sickbeard

EXPOSE 8081

# SickBeard Configuration
VOLUME /config

# Downloads directory
VOLUME /downloads

# TV directory
VOLUME /tv

# Add Sickbeard to runit
RUN mkdir /etc/service/sickbeard
ADD init/sickbeard.sh /etc/service/sickbeard/run
RUN chmod +x /etc/service/sickbeard/run
