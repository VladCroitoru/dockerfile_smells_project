FROM ubuntu:precise
MAINTAINER Dave Lu

# This is probably not needed
ENV DEBIAN_FRONTEND noninteractive

# Add universe repository
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise main universe" >> /etc/apt/sources.list

# Install things needed to add ROS repository
RUN apt-get update && apt-get install -y \
    apt-utils \
    wget \
    ca-certificates

# Install ROS Packages
RUN echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list
RUN wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -O - | apt-key add -
RUN apt-get update && apt-get install -y \
    ros-hydro-desktop-full \
    python-rosinstall \
    ros-hydro-turtlebot* \
    ros-hydro-rqt \
    ros-hydro-rqt-common-plugins

# Add user
RUN useradd davelu -m
RUN echo "davelu:qwer" | chpasswd

# Initialize ROS
RUN rosdep init
USER davelu
RUN rosdep update

# Setup catkin workspace
RUN bin/bash -c "echo 'source /opt/ros/hydro/setup.bash' >> ~/.bashrc && \
                 source /opt/ros/hydro/setup.bash && \
                 mkdir -p ~/catkin_ws/src && \
                 cd ~/catkin_ws/src && \
                 catkin_init_workspace && \
                 cd ~/catkin_ws/ && \
                 catkin_make && \
                 echo 'source ~/catkin_ws/devel/setup.bash' >> ~/.bashrc"

#############################################################################
############################ My Own Custom Stuff ############################
#############################################################################

# Install terminal emulator of choice and other utils
USER root
RUN apt-get update && apt-get install -y \
    terminator \
    ttf-inconsolata \
    iputils-ping \
    net-tools \
    sudo \
    vim
RUN sudo adduser davelu sudo
RUN chsh -s /bin/bash davelu
# Install graphics card driver
ADD ./nvidia /tmp/nvidia
RUN /tmp/nvidia/NVIDIA-Linux-x86_64-343.36.run -s -N --no-kernel-module
ADD ./config /home/davelu/.config/
RUN bin/bash -c "cat /home/davelu/.config/bash.extra >> /home/davelu/.bashrc"
RUN chown -R davelu /home/davelu/.config /home/davelu/.bashrc
USER davelu

#############################################################################
############################### Graphics Card ###############################
#############################################################################

# Connect to the host's display
ENV DISPLAY localhost:0

#############################################################################
############################### ROS Env Stuff ###############################
#############################################################################

# This should be run with
#  -v /tmp/.X11-unix:/tmp/.X11-unix       (to display on the host X server)
#  --privileged                           (to access the graphics card)

