FROM phusion/baseimage:0.11
MAINTAINER Specter <mike@mikeodriscoll.ca>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root

CMD ["/sbin/my_init"]

RUN usermod -u 99 nobody && \
usermod -g 100 nobody

RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe multiverse" && \
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse" && \
apt-get update -qq && \
apt-get upgrade -qq && \
# Install Dependencies
apt-get install -qq -y git python python-cheetah ca-certificates python-openssl wget unrar unzip && \
rm -rf /var/lib/apt/lists/*

# Install SickRage
RUN mkdir /opt/sickrage && \
git clone https://github.com/SickChill/SickChill.git -b master /opt/sickrage && \
chown -R nobody:users /opt/sickrage

EXPOSE 8081

# SickRage Configuration
VOLUME /config
# Downloads directory
VOLUME /downloads
# TV directory
VOLUME /tv

# Add SickRage to runit
RUN mkdir /etc/service/sickrage
ADD init/sickrage.sh /etc/service/sickrage/run
RUN chmod +x /etc/service/sickrage/run
