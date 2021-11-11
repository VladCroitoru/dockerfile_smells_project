FROM phusion/baseimage:0.9.15
MAINTAINER jondalar <alex@iphonedation.com>
#Forked from needo <needo@superhero.org>
#Based on the work of Eric Schultz <eric@startuperic.com>
#Thanks to Tim Haak <tim@haak.co.uk>

ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Install Plex
RUN apt-get -q update
RUN apt-get install -qy gdebi-core wget
#RUN wget -P /tmp https://downloads.plex.tv/plex-media-server/0.9.11.7.803-87d0708/plexmediaserver_0.9.11.7.803-87d0708_amd64.deb
RUN wget -P /tmp https://downloads.plex.tv/plex-media-server/0.9.12.4.1192-9a47d21/plexmediaserver_0.9.12.4.1192-9a47d21_amd64.deb
RUN gdebi -n /tmp/plexmediaserver_0.9.12.4.1192-9a47d21_amd64.deb
RUN echo plexmediaserver_0.9.12.4.1192-9a47d21_amd64.deb | awk -F_ '{print $2}' > /tmp/version
RUN rm -f /tmp/plexmediaserver_0.9.12.4.1192-9a47d21_amd64.deb

# we need an add to copy the plugins in!

# Fix a Debianism of plex's uid being 101
RUN usermod -u 999 plex
RUN usermod -g 100 plex

VOLUME /config
VOLUME /data
VOLUME /recordings

EXPOSE 32400

# Define /config in the configuration file not using environment variables
ADD plexmediaserver /etc/default/plexmediaserver

# Add firstrun.sh to execute during container startup
RUN mkdir -p /etc/my_init.d
ADD firstrun.sh /etc/my_init.d/firstrun.sh
RUN chmod +x /etc/my_init.d/firstrun.sh

#Add .bundles to /tmp so we can put them to the right place after first run!
RUN mkdir /tmp/plugins
ADD plugins  /tmp/plugins
RUN touch /tmp/novdrbundlesyet

# Add Plex to runit
RUN mkdir /etc/service/plex
ADD plex.sh /etc/service/plex/run
RUN chmod +x /etc/service/plex/run
