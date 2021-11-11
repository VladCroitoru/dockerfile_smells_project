FROM phusion/baseimage:18.04-1.0.0-amd64
MAINTAINER amacie 

## cloned from gfjardim  / https://github.com/gfjardim/docker-containers / <gfjardim@gmail.com>
## cloned from mnbf9rca  / https://github.com/mnbf9rca/cups-google-print

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################
# Set correct environment variables
ENV HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8" DEBIAN_FRONTEND="noninteractive" TERM="xterm"

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

#########################################
##         RUN INSTALL SCRIPT          ##
#########################################
RUN rm -rf /etc/service/sshd /etc/service/cron /etc/service/syslog-ng /etc/my_init.d/00_regen_ssh_host_keys.sh

# Install Dependencies
RUN curl -sSkL -o /tmp/epson-inkjet-printer-artisan-725-835-series_1.0.0-1lsb3.2_amd64.deb http://download.ebz.epson.net/dsc/op/stable/debian/dists/lsb3.2/main/binary-amd64/epson-inkjet-printer-artisan-725-835-series_1.0.0-1lsb3.2_amd64.deb \
# && curl -sSkL -o /tmp/google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
&& apt-get update -qq \
&& apt-get install -qy --force-yes \
 curl \
 cups \
 lsb \
 whois \
# /tmp/google-chrome-stable_current_amd64.deb \
 /tmp/epson-inkjet-printer-artisan-725-835-series_1.0.0-1lsb3.2_amd64.deb \
&& apt-get -qq -y autoclean \
&& apt-get -qq -y clean \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* || true 

ADD * /tmp/

# Create var/run/dbus, Disbale some cups backend that are unusable within a container, Clean install files
RUN chmod +x /tmp/*.sh \
&& /tmp/install.sh \
&& mkdir -p /var/run/dbus \
&& mv -f /usr/lib/cups/backend/parallel /usr/lib/cups/backend-available/ || true \
&& mv -f /usr/lib/cups/backend/serial /usr/lib/cups/backend-available/ || true \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* || true 

#########################################
##         EXPORTS AND VOLUMES         ##
#########################################
# Export volumes
VOLUME /config /etc/cups/ /var/log/cups /var/spool/cups /var/cache/cups /var/run/dbus
EXPOSE 631

