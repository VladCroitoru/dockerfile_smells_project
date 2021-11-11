FROM ubuntu:16.04

MAINTAINER Claudiu Paul RODEAN <paul.rodean@yopeso.com>

# disable interactive mod, to prevent pty errors
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y curl build-essential inetutils-ping

# Add php Ondrej PHP repo, for multiple versions of php, as for ubuntu 16.04 only version 7.0
# is available
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >> /etc/apt/sources.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-key 4F4EA0AAE5267A6C


# Add nodeJs official LTS repo
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -



# update && dist-upgrade
RUN apt-get update && apt-get -y dist-upgrade