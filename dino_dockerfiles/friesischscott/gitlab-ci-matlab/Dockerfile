FROM ubuntu:18.04

MAINTAINER Jasper Behrensdorf <behrensdorf@irz.uni-hannover.de>

ARG DEBIAN_FRONTEND=noninteractive

# Line 1: Matlab dependencies
# Line 2: Uploading reports to codecov.io
# Line 3: Needed to change MAC address for Matlab license
RUN apt-get update && apt-get install -y \
    libpng-dev libfreetype6-dev libblas-dev liblapack-dev gfortran build-essential xorg openjdk-8-jdk \
    curl git \
    iproute2

ENV PATH="/usr/local/MATLAB/from-host/bin:${PATH}"
