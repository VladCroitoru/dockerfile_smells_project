FROM phusion/baseimage:0.9.17
#Based on the work of Eric Schultz <eric@startuperic.com>
#Thanks to Tim Haak <tim@haak.co.uk>
#Based on plex container from needo <needo@superhero.org>
MAINTAINER Eric <edonaldson@draconrose.com>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Fix a Debianism of the nobody's uid being 65534
RUN usermod -u 99 nobody
RUN usermod -g 100 nobody

ADD sources.list /etc/apt/
RUN add-apt-repository -y -s ppa:mc3man/trusty-media
RUN apt-get update -qq
RUN apt-get install -qy ffmpeg nzbget wget unrar unzip p7zip

#Path to a directory that only contains the nzbget.conf
VOLUME /config
VOLUME /downloads

EXPOSE 6789

# Add edge.sh to execute during container startup
RUN mkdir -p /etc/my_init.d
ADD edge.sh /etc/my_init.d/edge.sh
ENV EDGE="v16.4"
RUN chmod +x /etc/my_init.d/edge.sh
RUN /etc/my_init.d/edge.sh

# Add firstrun.sh to execute during container startup
ADD firstrun.sh /etc/my_init.d/firstrun.sh
RUN chmod +x /etc/my_init.d/firstrun.sh

# Add nzbget to runit
RUN mkdir /etc/service/nzbget
ADD nzbget.sh /etc/service/nzbget/run
RUN chmod +x /etc/service/nzbget/run
