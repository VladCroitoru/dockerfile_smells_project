FROM phusion/baseimage
MAINTAINER Louis Dorard <louis@dorard.me>

# Make sure the package repository is up to date
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update

# Install some useful tools for development
RUN apt-get install -y wget git-core vim zsh

# Install ohmyzsh
RUN wget --no-check-certificate http://install.ohmyz.sh -O - | sh
RUN chsh -s /bin/zsh

# Form a set of standard directories
RUN mkdir -p /downloads
RUN mkdir -p /work
