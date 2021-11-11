FROM an0t8/dockergui:Xenial
MAINTAINER an0t8

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################
# Set correct environment variables
ENV USER_ID=99
ENV GROUP_ID=100
ENV TERM="xterm"
ENV CP_PRO_VERSION="4.9.0_1436674888490_33"

# Gui App Name default is "GUI_APPLICATION"
ENV APP_NAME="Crashplan"

#Default resolution, change if you like
ENV WIDTH=1280
ENV HEIGHT=720

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

#########################################
##          GUI APP INSTALL            ##
#########################################

ADD ./files/install.sh /tmp/install.sh
RUN chmod +x /tmp/install.sh && sleep 1 && /tmp/install.sh && rm /tmp/install.sh

#########################################
##         EXPORTS AND VOLUMES         ##
#########################################
VOLUME /data /config
EXPOSE 4243 3389
