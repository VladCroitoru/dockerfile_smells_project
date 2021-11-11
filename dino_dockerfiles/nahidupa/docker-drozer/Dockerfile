# This docker file has https://www.mwrinfosecurity.com/products/drozer/ 
# its installed drozer (Debian/Ubuntu Archive) https://www.mwrinfosecurity.com/system/assets/931/original/drozer_2.3.4.deb 
# a local cache are in side deb directory

FROM ubuntu:14.04
MAINTAINER nahidupa@gmail.com
# Install packages  
RUN apt-get update \
 && apt-get install -y git python python-dev python-protobuf python-openssl python-twisted openjdk-7-jdk 
#drozer looking for this file.  
RUN touch /etc/bash_completion

VOLUME /work
COPY ./deb /work

WORKDIR /work
# Install the console
RUN dpkg -i drozer_2.4.4.deb
RUN rm *.deb

# Clean up 
RUN apt-get autoremove
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
