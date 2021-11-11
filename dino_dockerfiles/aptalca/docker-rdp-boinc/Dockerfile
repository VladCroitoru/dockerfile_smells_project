
# Builds a docker gui image
FROM hurricane/dockergui:xvnc

MAINTAINER aptalca

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################

# Set environment variables

# User/Group Id gui app will be executed as default are 99 and 100
ENV USER_ID=99
ENV GROUP_ID=100

# Gui App Name default is "GUI_APPLICATION"
ENV APP_NAME="Boinc"

# Default resolution, change if you like
ENV WIDTH=1280
ENV HEIGHT=720

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

RUN \
#########################################
##    REPOSITORIES AND DEPENDENCIES    ##
#########################################
echo 'deb http://archive.ubuntu.com/ubuntu trusty main universe restricted' > /etc/apt/sources.list && \
echo 'deb http://archive.ubuntu.com/ubuntu trusty-updates main universe restricted' >> /etc/apt/sources.list && \

# Install packages needed for app
export DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive && \
apt-get update && \
apt-get install -y \
libnotify4 \
libwxgtk2.8-dev \
libxss1
#########################################
##          GUI APP INSTALL            ##
#########################################

# Install steps for X app
ADD firstrun.sh /etc/my_init.d/firstrun.sh
RUN chmod +x /etc/my_init.d/firstrun.sh && \
mkdir -p /nobody/boinc && \
cd /nobody/boinc && \
wget http://boinc.berkeley.edu/dl/boinc_7.2.42_x86_64-pc-linux-gnu.sh

# Copy X app start script to right location
COPY startapp.sh /startapp.sh

#########################################
##         EXPORTS AND VOLUMES         ##
#########################################

# Place whater volumes and ports you want exposed here:
VOLUME ["/config"]
EXPOSE 3389 8080
