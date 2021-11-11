# Automatic Video Transcoding Docker
#  For Unraid
#
# v 1.0 - Initial Setup 4/2/17
#

# Using phusion baseimage
FROM phusion/baseimage:latest

MAINTAINER Valherun

# Install startup script
# 	- executes required setup on startup
RUN mkdir -p /etc/my_init.d/
COPY init/Startup.sh /etc/my_init.d/
RUN chmod +x /etc/my_init.d/Startup.sh

# Drop in automation and services scripts
RUN mkdir -p /transcoder-files
COPY init/* /transcoder-files/

# Now we need to setup access to required folders
# /config is the folder that will hold our main transcoding script
#	- holds the automation scripts
#	- allows changes to automation without having to access docker
#
# /media/transcoder
#	- the holding spot for stuff you need to transcode
#
# setup folders within docker, but VOLUME links them to external folders/drives
VOLUME ["/media/transcoder", "/config"]

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
