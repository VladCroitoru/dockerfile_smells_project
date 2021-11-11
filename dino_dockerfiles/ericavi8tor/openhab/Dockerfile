#Base configuration nicked from github.com/limetech/dockerapp-plex

FROM phusion/baseimage:0.9.16
MAINTAINER ericavi8tor

# Set correct environment variables
ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"

# Install OpenHab
ADD install.sh /
RUN bash /install.sh

# Run on start
ADD firstrun.sh /etc/my_init.d/firstrun.sh
RUN chmod +x /etc/my_init.d/firstrun.sh

# Symlink USB devices
# ADD files/50-usb-serial.rules /etc/udev/rules.d/50-usb-serial.rules
# RUN chmod +x /etc/udev/rules.d/50-usb-serial.rules

# Custom startup for symlink support
# ADD files/start.sh /opt/openhab/start.sh
# RUN chmod +x /opt/openhab/start.sh

# Custom Config
ADD files/openhab.cfg /opt/openhab/configurations/openhab.cfg
RUN chmod +x /opt/openhab/configurations/openhab.cfg

VOLUME /config

EXPOSE 8080 8443 5555 9001

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]
