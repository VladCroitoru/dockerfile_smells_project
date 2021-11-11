FROM phusion/baseimage:0.9.18
MAINTAINER gfjardim <gfjardim@gmail.com>

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################
# Set correct environment variables
ENV CP_VERSION="4.6.0"
ENV USER_ID="0" GROUP_ID="0" TERM="xterm"

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

#########################################
##         RUN INSTALL SCRIPT          ##
#########################################
ADD ./files /files/
## RUN /bin/bash /files/install.sh

# Disable SSH
RUN rm -rf /etc/service/sshd /etc/service/cron /etc/my_init.d/00_regen_ssh_host_keys.sh

#########################################
##    REPOSITORIES AND DEPENDENCIES    ##
#########################################

# Repositories
RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu/ trusty universe multiverse" && \
    add-apt-repository "deb http://archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse"
    
# Add Oracle JAVA and accept it's license
RUN add-apt-repository ppa:webupd8team/java && \
    echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | sudo /usr/bin/debconf-set-selections

# Local mirror
RUN mkdir /opt/apt-select && \
    URL=$(curl -sL https://github.com/jblakeman/apt-select/releases/latest | grep -Po "/jblakeman/apt-select/archive/.*.tar.gz") && \
    curl -sL "https://github.com${URL}" | tar zx -C /opt/apt-select --strip-components=1 && \
    apt-get update -qq && apt-get -qy --force-yes install python3-bs4 && \
    cd /opt && python3 /opt/apt-select/apt-select.py -t 3 -m up-to-date && \
    [ -f /opt/sources.list ] && mv /opt/sources.list /etc/apt/sources.list

# Install Dependencies
# Install CrashPlan dependencies
RUN apt-get update -qq & apt-get install -qy --force-yes --no-install-recommends \
                grep \
                python-xdg \
                sed \
                cpio \
                gzip \
                wget \
                oracle-java8-installer \
                gtk2-engines-murrine \
                ttf-ubuntu-font-family

# Install window manager and x-server
RUN apt-get install -qy --force-yes --no-install-recommends \
                x11-xserver-utils \
                openbox \
                xfonts-base \
                xfonts-100dpi \
                xfonts-75dpi \
                libfuse2 \
                xbase-clients

# Install noVNC dependencies
RUN apt-get install -qy --force-yes --no-install-recommends \
                python \
                git

#########################################
##  FILES, SERVICES AND CONFIGURATION  ##
#########################################

# CrashPlan Service
RUN mkdir -p /etc/service/crashplan /etc/service/crashplan/control && \
    cp /files/crashplan/service.sh /etc/service/crashplan/run
    cp /files/crashplan/service_stop.sh /etc/service/crashplan/control/t

# CrashPlan Desktop
RUN cp /files/crashplan/desktop.sh /opt/startapp.sh && \
    cp /files/crashplan/desktop_stop.sh /opt/stopapp.sh && \
    chmod +x /opt/startapp.sh /opt/stopapp.sh

# noVNC Service
RUN mkdir -p /etc/service/novnc && \
    cp /files/novnc/service.sh /etc/service/novnc/run

# Openbox Service
RUN mkdir -p /etc/service/openbox  /etc/service/openbox/control/ && \
    cp /files/openbox/service.sh /etc/service/openbox/run && \
    cp /files/openbox/service_stop.sh /etc/service/openbox/control/t

# Openbox Autostart
RUN mkdir -p /nobody/.config/openbox /nobody/.cache && \
    cp /files/openbox/autostart.sh /nobody/.config/openbox/autostart && \
    cp /files/openbox/rc.xml /nobody/.config/openbox/rc.xml

# TigerVNC Service
RUN mkdir -p /etc/service/tigervnc && \
    cp /files/tigervnc/service.sh /etc/service/tigervnc/run

# Config File
RUN mkdir -p /etc/my_init.d && \
    cp /files/00_config.sh /etc/my_init.d/00_config.sh
    cp /files/01_config.sh /etc/my_init.d/01_config.sh

RUN chmod -R +x /etc/service/ /etc/my_init.d/

#########################################
##             INSTALLATION            ##
#########################################

# Install Crashplan
RUN /bin/bash /files/crashplan/install.sh

# Install TigerVNC
RUN /bin/bash /files/tigervnc/install.sh

# Install noVNC
RUN /bin/bash /files/novnc/install.sh

#########################################
##                 CLEANUP             ##
#########################################

# Clean APT install files
RUN apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /var/cache/* /var/tmp/*


#########################################
##         EXPORTS AND VOLUMES         ##
#########################################
VOLUME /data /config
EXPOSE 4243 4242 4280
