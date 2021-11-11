FROM python:3.4.4

MAINTAINER EngageNExecute code@engagenexecute.com

# Install packages.
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        locales \
        python-dev \
        cmake \
        libpq-dev \
        python-pip \
        git-core \
        libopencv-dev \
        python-opencv \
        python-numpy

# Set UTF-8 as locales
RUN dpkg-reconfigure locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8

# ENV UTF-8
ENV LC_ALL C.UTF-8

# Disable warning driver1394 (camera)
RUN ln /dev/null /dev/raw1394
