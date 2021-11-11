FROM phusion/baseimage:0.9.16
MAINTAINER needo <needo@superhero.org>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV TERM xterm


# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Fix a Debianism of the nobody's uid being 65534
RUN usermod -u 99 nobody
RUN usermod -g 100 nobody

ADD sources.list /etc/apt/
RUN add-apt-repository ppa:mc3man/trusty-media -y
RUN apt-get update -qq
RUN apt-get install -qy ffmpeg nzbget wget unrar mc unzip p7zip-full

#Path to a directory that only contains the nzbget.conf
VOLUME /config
VOLUME /downloads

EXPOSE 6789

# Add edge.sh to execute during container startup
RUN mkdir -p /etc/my_init.d
ADD edge.sh /etc/my_init.d/edge.sh
RUN chmod +x /etc/my_init.d/edge.sh

# Add firstrun.sh to execute during container startup
ADD firstrun.sh /etc/my_init.d/firstrun.sh
RUN chmod +x /etc/my_init.d/firstrun.sh

# Add nzbget to runit
RUN mkdir /etc/service/nzbget
ADD nzbget.sh /etc/service/nzbget/run
RUN chmod +x /etc/service/nzbget/run
