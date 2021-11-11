FROM phusion/baseimage:0.9.16
MAINTAINER Kierran McPherson <kierranm@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

# install git
RUN apt-get update && apt-get install -y \
  git-core \
  python

# clone the git repo into the /couchpotato directory
RUN git clone https://github.com/RuudBurger/CouchPotatoServer.git /couchpotato

# expose the couch potato port
EXPOSE 5050

# set up the mount point for external data
VOLUME /couchpotato-data

# copy across the defaults file
ADD Assets/couchpotato-defaults /etc/default/couchpotato
# copy across the default config.ini
ADD Assets/config.ini /tmp/config.ini

# Setup the config for container startup
RUN mkdir -p /etc/my_init.d
ADD Assets/config.sh /etc/my_init.d/config.sh
RUN chmod a+x /etc/my_init.d/config.sh

# Set up the runit script
RUN mkdir -p /etc/service/couchpotato
ADD Assets/couchpotato.sh /etc/service/couchpotato/run
RUN chmod a+x /etc/service/couchpotato/run

# use phusion/baseimage init system
CMD ["/sbin/my_init"]
