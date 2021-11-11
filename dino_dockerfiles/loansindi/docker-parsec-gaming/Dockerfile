# x11docker/xfce
# 
# Run XFCE desktop in docker. 
# Use x11docker to run image. 
# Get x11docker from github: 
#   https://github.com/mviereck/x11docker 
#
# Examples: x11docker --desktop x11docker/xfce
#           x11docker x11docker/xfce thunar 

FROM debian:stretch
ENV DEBIAN_FRONTEND noninteractive

RUN echo "deb http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu trusty main" >> /etc/apt/sources.list
RUN echo "deb-src http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu trusty main" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y apt-utils \
	dbus-x11 x11-utils \
	x11-xserver-utils \
	procps psmisc \
# OpenGL support
	mesa-utils \
	mesa-utils-extra \
	libxv1

# Language/locale settings
ENV LANG=en_US.UTF-8
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" > /etc/default/locale
RUN apt-get install -y locales

# some utils to have proper menus, mime file types etc.
RUN apt-get install -y --no-install-recommends xdg-utils xdg-user-dirs
RUN apt-get install -y menu menu-xdg mime-support desktop-file-utils desktop-base

# Xfce
RUN apt-get install -y --no-install-recommends xfce4 
RUN apt-get install -y xfce4-terminal mousepad xfce4-notifyd 

# includes GTK3 broadway support for HTML5 web applications
RUN apt-get install -y --no-install-recommends libgtk-3-bin


# clean up
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get install -y --allow-unauthenticated --no-install-recommends        initramfs-tools \
    libcairo2 \
    libfreetype6 \
    libgdk-pixbuf2.0-0 \
    libgl1-mesa-glx \
    libgl1 \
    libglib2.0-0 \
    libgtk2.0-0 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libsm6 \
    libsndio6.1 \
    wget \
    libasound2  \
    alsa-utils \
    alsa-oss \
    software-properties-common \
    gnupg \
    nvidia-387 \
    pulseaudio \
    xserver-xorg-core
RUN wget --no-check-certificate https://s3.amazonaws.com/parsec-build/package/parsec-linux.deb
RUN dpkg -i parsec-linux.deb
RUN apt-get install -y openbox

# create startscript 
RUN echo '#! /bin/bash\n\
[ -e "$HOME/.config" ] || cp -R /etc/skel/. $HOME/ \n\
exec openbox-session\n\
' > /usr/local/bin/start 
RUN chmod +x /usr/local/bin/start 
CMD start
