############################################################
# Dockerfile for Ookla Host Server
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Andrew Gee <agee@techfutures.co>

# Update the repository sources list and install wget
RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

################## BEGIN INSTALLATION ######################
# Install Ookla Host Server
# Ref: http://www.ookla.com/support/a26325856prise/

RUN wget http://install.speedtest.net/ooklaserver/ooklaserver.sh
RUN chmod a+x ooklaserver.sh
RUN ./ooklaserver.sh install -f

##################### INSTALLATION END #####################

# Expose the default port
EXPOSE 8080
