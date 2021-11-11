FROM nodesource/jessie:5.8.0
MAINTAINER Christian Brandlehner <christian@brandlehner.at>

##################################################
# Set environment variables                      #
##################################################

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

##################################################
# Install tools                                  #
##################################################

RUN apt-get update
RUN apt-get install -y apt-utils apt-transport-https locales
RUN apt-get install -y curl wget git python build-essential make g++ libkrb5-dev vim net-tools nano
RUN apt-get install -y avahi-daemon avahi-discover libnss-mdns libavahi-compat-libdnssd-dev
COPY avahi-daemon.conf /etc/avahi/avahi-daemon.conf
RUN alias ll='ls -alG'

##################################################
# Install homebridge                             #
##################################################

RUN npm install -g homebridge --unsafe-perm

# depending on your config.json you have to add your modules here!
#RUN npm install -g homebridge-philipshue --unsafe-perm
#RUN npm install -g homebridge-ninjablock-temperature --unsafe-perm
#RUN npm install -g homebridge-ninjablock-humidity --unsafe-perm
#RUN npm install -g homebridge-ninjablock-alarmstatedevice --unsafe-perm
#RUN npm install -g homebridge-luxtronik2 --unsafe-perm
RUN npm install -g homebridge-synology homebridge-sonos homebridge-nest homebridge-lifx --unsafe-perm

#RUN npm install -g homebridge-mqttswitch --unsafe-perm
#RUN npm install -g homebridge-edomoticz --unsafe-perm

##################################################
# Start                                          #
##################################################

USER root
RUN mkdir -p /var/run/dbus

ADD image/run.sh /root/run.sh

EXPOSE 5353 51826
CMD ["/root/run.sh"]
