# Builds a docker gui image
FROM cgspeck/dockergui:x11rdp1.3

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################

# Set environment variables

# User/Group Id gui app will be executed as default are 99 and 100
ENV USER_ID=99
ENV GROUP_ID=100

# Gui App Name default is "GUI_APPLICATION"
ENV APP_NAME OKULAR

# Default resolution, change if you like
ENV WIDTH=1600
ENV HEIGHT=900

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

#########################################
##    REPOSITORIES AND DEPENDENCIES    ##
#########################################
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ xenial main universe restricted' > /etc/apt/sources.list
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ xenial-updates main universe restricted' >> /etc/apt/sources.list

# Install packages needed for app
RUN apt-get update
RUN apt-get install -y okular okular-extra-backends

#########################################
##          GUI APP INSTALL            ##
#########################################

# Install steps for X app

# Copy X app start script to right location
COPY firstrun.sh /etc/my_init.d/firstrun.sh
RUN chmod +x /etc/my_init.d/firstrun.sh
COPY startapp.sh /startapp.sh

#########################################
##         EXPORTS AND VOLUMES         ##
#########################################

VOLUME ["/config"]
EXPOSE 3389 8080
