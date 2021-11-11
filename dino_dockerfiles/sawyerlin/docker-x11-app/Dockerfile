FROM ubuntu:16.04
MAINTAINER Sawyer LIN <sawyer.lin@gmail.com>

RUN apt-get update -y
RUN apt-get upgrade -y

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y xpra rox-filer openssh-server pwgen xserver-xephyr xdm fluxbox xvfb sudo software-properties-common python-software-properties build-essential libgl1-mesa-dev

RUN sed -i 's/DisplayManager.requestPort/!DisplayManager.requestPort/g' /etc/X11/xdm/xdm-config
RUN sed -i '/#any host/c\*' /etc/X11/xdm/Xaccess
RUN echo X11Forwarding yes >> /etc/ssh/ssh_config

RUN sed -i 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd

RUN dpkg-divert --local --rename --add /sbin/initctl && ln -sf /bin/true /sbin/initctl

RUN apt-get -y install fuse || :
RUN rm -rf /var/lib/dpkg/info/fuse.postinst
RUN apt-get -y install fuse

RUN apt-get install -y libgstreamer* gstreamer* pulseaudio libfreetype6-dev libx11-dev libxext-dev libxfixes-dev libxi-dev libxrender-dev libx11-xcb-dev libfreetype6-dev
