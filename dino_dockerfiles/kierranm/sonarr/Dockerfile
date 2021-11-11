FROM phusion/baseimage:0.9.16
MAINTAINER Kierran McPherson <kierranm@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

ENV HOME /root

RUN ln -s -f /bin/true /usr/bin/chfn

# Install Sonarr
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC
RUN echo "deb http://update.nzbdrone.com/repos/apt/debian master main" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
    libmono-cil-dev \
    python \
    nzbdrone

# expose the Sonarr port
EXPOSE 8989

# Mount the data volume, should contain the config, TV shows and other directories
VOLUME /sonarr-data

# Set up the init script
RUN mkdir -p /etc/my_init.d
ADD Assets/config.sh /etc/my_init.d/config.sh
RUN chmod a+x /etc/my_init.d/config.sh

# Set up the runit script
RUN mkdir -p /etc/service/sonarr
ADD Assets/sonarr.sh /etc/service/sonarr/run
RUN chmod a+x /etc/service/sonarr/run

# use phusion/baseimage init system
CMD ["/sbin/my_init"]
