# Builds a docker gui image
FROM hurricane/dockergui:xvnc

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################

# Set environment variables

# User/Group Id gui app will be executed as default are 99 and 100
ENV USER_ID=99
ENV GROUP_ID=100

# Gui App Name default is "GUI_APPLICATION"
ENV APP_NAME atom

# Default resolution, change if you like
ENV WIDTH=1280
ENV HEIGHT=720

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

#########################################
##    REPOSITORIES AND DEPENDENCIES    ##
#########################################
RUN \
echo 'deb http://archive.ubuntu.com/ubuntu trusty main universe restricted' > /etc/apt/sources.list && \
echo 'deb http://archive.ubuntu.com/ubuntu trusty-updates main universe restricted' >> /etc/apt/sources.list && \
export DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive

# Install packages needed for app

#########################################
##          GUI APP INSTALL            ##
#########################################

ENV ATOM_VERSION v1.23.2

# Install steps for X app
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    fakeroot \
    gconf2 \
    gconf-service \
    git \
    gvfs-bin \
    libasound2 \
    libcap2 \
    libgconf-2-4 \
    libgtk2.0-0 \
    libnotify4 \
    libnss3 \
    libxkbfile1 \
    libxss1 \
    libxtst6 \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    python \
    xdg-utils && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  curl -L https://github.com/atom/atom/releases/download/${ATOM_VERSION}/atom-amd64.deb > /tmp/atom.deb && \
  dpkg -i /tmp/atom.deb && \
  rm -f /tmp/atom.deb && \
  useradd -d /home/atom -m atom && \
  cp /usr/lib/x86_64-linux-gnu/libxcb.so.1 /usr/share/atom/ && \
  sed -i 's/BIG-REQUESTS/_IG-REQUESTS/' /usr/share/atom/libxcb.so.1

# Copy X app start script to right location
COPY startapp.sh /startapp.sh

#########################################
##         EXPORTS AND VOLUMES         ##
#########################################

# Place whater volumes and ports you want exposed here:
VOLUME ["/saved"]
EXPOSE 3389 8080
