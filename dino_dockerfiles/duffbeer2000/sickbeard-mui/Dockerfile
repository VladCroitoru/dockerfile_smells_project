FROM phusion/baseimage:0.9.11
MAINTAINER duffbeer2000 (thx to needo)
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Fix a Debianism of the nobody's uid being 65534
RUN usermod -u 99 nobody
RUN usermod -g 100 nobody

RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe multiverse"
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse"
RUN apt-get update -q

# Install Dependencies
RUN apt-get install -qy python python-cheetah ca-certificates wget unrar

# Install SickBeard
RUN mkdir /opt/sickbeard
RUN wget https://github.com/cytec/Sick-Beard/tarball/6c60e5e35f9b636563c8cf28b1225ea2ba26366a -O /tmp/midgetspy-SickBeard-0e81fe9baf.tar.gz
RUN tar -C /opt/sickbeard -xvf /tmp/midgetspy-SickBeard-0e81fe9baf.tar.gz --strip-components 1
RUN chown nobody:users /opt/sickbeard

EXPOSE 8081

# SickBeard Configuration
VOLUME /config

# Downloads directory
VOLUME /downloads

# TV directory
VOLUME /tv

# Add edge.sh to execute during container startup
RUN mkdir -p /etc/my_init.d
ADD edge.sh /etc/my_init.d/edge.sh
RUN chmod +x /etc/my_init.d/edge.sh

# Add Sickbeard to runit
RUN mkdir /etc/service/sickbeard
ADD sickbeard.sh /etc/service/sickbeard/run
RUN chmod +x /etc/service/sickbeard/run
