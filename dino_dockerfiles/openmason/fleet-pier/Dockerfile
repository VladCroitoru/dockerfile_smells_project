# all minimum required utilities and daemons
#
# Usage:
# docker build -t openmason/fleet-pier .
#
#
FROM openmason/fleet-base:latest
MAINTAINER el aras<openmason@gmail.com>

# env variables
ENV DEPLOY_USER openmason
#ENV HOME /home/$DEPLOY_USER

# Any ppa repositories go here

# required dev packages
RUN \
  apt-get update; \
  apt-get install -yq libevent-dev libzmq-dev  --no-install-recommends; \
  apt-get clean

# required scripting/daemon packages
RUN \
  apt-get update; \
  apt-get install -yq  nodejs --no-install-recommends; \
  apt-get install -yq  openssh-server  ssh-import-id  --no-install-recommends; \
  pip install --upgrade circus; \
  mkdir /var/run/sshd; \
  apt-get clean

# create deploy user
RUN useradd -m -d /home/$DEPLOY_USER -p $DEPLOY_USER $DEPLOY_USER && adduser $DEPLOY_USER sudo && chsh -s /bin/bash $DEPLOY_USER
#USER $DEPLOY_USER
RUN ssh-import-id gh:$DEPLOY_USER
