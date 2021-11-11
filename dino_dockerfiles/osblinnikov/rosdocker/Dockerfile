# Name: rosDocker
# Description: installs ROS-indigo base in ubuntu trusty environment
#
# VERSION       1.1
#

# Use the ubuntu base image
FROM ubuntu:trusty

MAINTAINER Oleg Blinnikov, osblinnikov@gmail.com

# make sure the package repository is up to date
RUN apt-get -y update
RUN apt-get install -y debian-keyring debian-archive-keyring

# install ROS key
RUN apt-get install -y wget
RUN wget --no-check-certificate https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -O - | apt-key add -

# for TESTS of exposing port
RUN apt-get install -y netcat

# update ros repository
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list'
RUN sh -c 'echo "deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu trusty main" > /etc/apt/sources.list.d/node-latest.list'
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B9316A7BC7917B12
RUN apt-get update

# install ROS
RUN apt-get install -y ros-indigo-ros-base

# enables you to easily download many source trees for ROS packages with one command
RUN apt-get install -y python-rosinstall

# Install additional useful packages
RUN apt-get install -y bash-completion git build-essential vim tmux

# Initialise rosdep
RUN rosdep init

# Adding vnc server
# no Upstart or DBus
# https://github.com/dotcloud/docker/issues/1724#issuecomment-26294856
RUN apt-mark hold initscripts udev plymouth mountall
RUN dpkg-divert --local --rename --add /sbin/initctl && ln -sf /bin/true /sbin/initctl

RUN apt-get install -y --force-yes --no-install-recommends supervisor \
        openssh-server pwgen sudo vim-tiny \
        net-tools \
        lxde x11vnc xvfb \
        gtk2-engines-murrine ttf-ubuntu-font-family \
        nodejs \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*


ADD noVNC /noVNC
ADD supervisord.conf /

# Launch bash when launching the container
ADD startcontainer /usr/local/bin/startcontainer
RUN chmod 755 /usr/local/bin/startcontainer

# Now create the ros user itself
RUN adduser --gecos "ROS User" --disabled-password ros
RUN usermod -a -G dialout ros

RUN mkdir /var/run/sshd

ADD 99_aptget /etc/sudoers.d/99_aptget
RUN chmod 0440 /etc/sudoers.d/99_aptget && chown root:root /etc/sudoers.d/99_aptget

RUN echo "    ForwardX11Trusted yes\n" >> /etc/ssh/ssh_config

# And, as that user...
USER ros

# HOME needs to be set explicitly. Without it, the HOME environment variable is
# set to "/"
RUN HOME=/home/ros rosdep update

# Create a ROS workspace for the ROS user.
RUN mkdir -p /home/ros/workspace/src
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; catkin_init_workspace /home/ros/workspace/src'
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd /home/ros/workspace; catkin_make'
ADD bashrc /.bashrc
ADD bashrc /home/ros/.bashrc

RUN mkdir -p /home/ros/Desktop
ADD xterm /home/ros/Desktop/

CMD ["/bin/bash"]
ENTRYPOINT ["/usr/local/bin/startcontainer"]



