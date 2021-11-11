FROM ubuntu:trusty

MAINTAINER Anteneh Aklilu "reachanteneh@gmail.com"

#Avoid interactive post-install configs
ARG DEBIAN_FRONTEND=noninteractive

# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y \
 unzip \
 supervisor \
 wget \
 asterisk \
 asterisk-doc \
 asterisk-dev \
 asterisk-ooh323 \
 libasound2-plugins \
 alsa-utils \
 libsox-fmt-all \
 speex

RUN apt-get clean && \
  	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
	
	#Create directories required by asterisk
RUN	mkdir -p /var/log/asterisk && \
	mkdir -p /var/spool/asterisk && \
	mkdir -p /usr/share/asterisk

	# Update max number of open files.
RUN sed -i -e 's/# MAXFILES=/MAXFILES=/' /usr/sbin/safe_asterisk
	
	# Set tty
RUN sed -i 's/TTY=9/TTY=/g' /usr/sbin/safe_asterisk

RUN chown asterisk:asterisk /var/run/asterisk && \
	chown -R asterisk:asterisk /etc/asterisk/ && \
	chown -R asterisk:asterisk /var/lib/asterisk && \
	chown -R asterisk:asterisk /var/log/asterisk && \ 
	chown -R asterisk:asterisk /var/spool/asterisk && \
	chown -R asterisk:asterisk /usr/share/asterisk

#Add custom configs
COPY conf/* /etc/asterisk/

#Add custom sounds
COPY sounds/* /usr/share/asterisk/sounds/

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#Make asterisk ports open
EXPOSE 5060 5038

VOLUME [/usr/share/asterisk, /etc/asterisk, /var/log/asterisk, /var/spool/asterisk]

CMD ["/usr/bin/supervisord"]
