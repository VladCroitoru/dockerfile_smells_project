# Set the base image
FROM ubuntu:14.04

# Dockerfile Maintainer
MAINTAINER Person Lin <personlin@gmail.com>

# Run update and install software
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    gfortran \
    cmake \
    wget \
    git

# Git clone
RUN git clone https://github.com/abrahamson/HAZ.git /home/HAZ && cd /home/HAZ && git checkout develop

# Build
RUN mkdir /home/HAZ/build && cd /home/HAZ/build && cmake .. && make

# Set path
ENV PATH="/home/HAZ/build:${PATH}"

# Define working directory.
WORKDIR /home/HAZ/build
