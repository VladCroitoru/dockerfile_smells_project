FROM osrf/ros:indigo-desktop-full
MAINTAINER Wilbert van de Ridder wilbert.ridder+drig7@gmail.com

# install ros and gazebo packages
RUN apt-get update && apt-get install -y \
    build-essential tree curl python-rosdep python-rosinstall-generator python-wstool python-rosinstall wget \
    && apt-get remove -y gazebo2 \
    && rm /etc/ros/rosdep/sources.list.d/20-default.list \
    && rosdep init && rosdep update \
    # Install gazebo 7
    && curl -ssL http://get.gazebosim.org | sh \
    # Install gazebo-ros packages
    && apt-get install -y ros-indigo-gazebo7-ros-pkgs ros-indigo-gazebo7-ros-control \
    && wget https://raw.githubusercontent.com/osrf/osrf-rosdep/master/gazebo7/00-gazebo7.list -O /etc/ros/rosdep/sources.list.d/00-gazebo7.list \
    && rosdep update \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
