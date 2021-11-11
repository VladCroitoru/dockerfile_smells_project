FROM base/archlinux:latest
MAINTAINER middleagedman

# additional files
##################

# add install bash script
ADD install.sh /root/install.sh

# install app
#############

# run bash script to update base image, set locale, install supervisor and cleanup
RUN chmod +x /root/install.sh && /bin/bash /root/install.sh

#
#####

# set environment variables
ENV HOME=/home/nobody TERM=vt220 LANG=en_US.UTF-8

# additional files
##################

# add supervisor configuration file
ADD supervisor.conf /etc/supervisor.conf
