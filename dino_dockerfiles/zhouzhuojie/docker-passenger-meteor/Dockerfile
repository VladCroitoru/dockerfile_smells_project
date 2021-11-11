FROM phusion/passenger-nodejs
MAINTAINER Zhuojie Zhou <me@zzj.im>

# Set correct environment variables
ENV HOME /root

# Disable ssh on container
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Install Node (last version, from node source repo)
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN sudo apt-get install -y build-essential nodejs python

# Install Meteor
RUN curl https://install.meteor.com/ | sh

# Clean up APT and /tmp when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN sudo npm install -g phantomjs
ADD ./dev.sh /home/app/dev.sh
ADD ./prod.sh /home/app/prod.sh
