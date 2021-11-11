FROM ubuntu:12.04
MAINTAINER Moritz Tenorth <knowrob@tenorth.de>

RUN apt-get -y update
RUN apt-get -y install git

# RUN useradd -m -d /home/ros -p ros ros && adduser ros sudo && chsh -s /bin/bash ros

# Create data directory
RUN mkdir -p /home/ros/knowrob_data
# RUN chown -R ros:ros /home/ros

WORKDIR /home/ros/knowrob_data
ADD . /home/ros/knowrob_data/

# Create knowrob_data data volume
VOLUME /home/ros/knowrob_data
