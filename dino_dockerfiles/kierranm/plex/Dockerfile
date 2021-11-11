FROM phusion/baseimage:0.9.16
MAINTAINER Kierran McPherson <kierranm@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

ENV HOME /root

RUN ln -s -f /bin/true /usr/bin/chfn

RUN apt-get -q update && apt-get install -qy \
    gdebi-core \
    wget
ADD Assets/installplex.sh /
RUN bash /installplex.sh

EXPOSE 32400

VOLUME /tv
VOLUME /movies
VOLUME /music
VOLUME /photos
VOLUME /videos
VOLUME /config

#copy across the default plex configuration
ADD Assets/plexmediaserver /etc/default/plexmediaserver

# Set up the init script
RUN mkdir -p /etc/my_init.d
ADD Assets/config.sh /etc/my_init.d/config.sh
RUN chmod a+x /etc/my_init.d/config.sh

# Set up the runit script
RUN mkdir -p /etc/service/plex
ADD Assets/plex.sh /etc/service/plex/run
RUN chmod a+x /etc/service/plex/run

# use phusion/baseimage init system
CMD ["/sbin/my_init"]
