# Start with Ubuntu base image
FROM ubuntu:18.10
MAINTAINER Lawrence Cabal <lawcab@gmail.com>

# Install LXDE, VNC server and Firefox
RUN apt-get update
RUN apt-get -yqq upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
  lxde-core \
  lxterminal \
  expect \
  wget \
  tightvncserver \
  ca-certificates \
  curl \
  dnsutils \
  man \
  openssl \
  unzip \
  software-properties-common \
#  python-software-properties \
  openssh-client \
  git
  
# Set user for VNC server (USER is only for build)
ENV USER root
# Set default password
COPY password.sh /opt/
RUN cd /opt \
&& chmod u+x password.sh
RUN /opt/password.sh
# Expose VNC port
EXPOSE 5901

# Set the locale
#RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

COPY vnc.sh /opt/
RUN cd /opt \
&& chmod u+x vnc.sh
