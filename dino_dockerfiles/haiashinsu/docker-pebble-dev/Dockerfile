############################################################
# Dockerfile to build container images for Pebble watch dev
# Based on Ubuntu
############################################################

FROM ubuntu:14.04
MAINTAINER Hyacinth Cruz <https://github.com/haiashinsu>

# define
ENV PEBBLE_SDK_VERSION 4.4.1
ENV PEBBLE_FILE pebble-sdk-$PEBBLE_SDK_VERSION-linux64
ENV PEBBLE_PATH /opt/pebble-dev
ENV PEBBLE_HOME $PEBBLE_PATH/$PEBBLE_FILE
ENV PATH $PEBBLE_HOME/bin:$PATH

# update system, get base packages and install python
RUN apt-get update && apt-get install -y curl git python2.7-dev python-pip

# emulator dependencies
RUN apt-get install -y libsdl1.2debian libfdt1 libpixman-1-0

# get pebble sdk
RUN mkdir -p $PEBBLE_PATH
RUN curl -sSL https://s3.amazonaws.com/assets.getpebble.com/pebble-tool/$PEBBLE_FILE.tar.bz2 | tar -v -C $PEBBLE_PATH -jx

# install pip, virtualenv and python library dependencies locally
WORKDIR $PEBBLE_HOME
RUN /bin/bash -c " \
    pip install virtualenv && \
    virtualenv --no-site-packages .env && \
    source .env/bin/activate && \
    pip install -r requirements.txt && \
    deactivate \
    "

RUN /bin/bash -c " \
    mkdir -p /home/pebble/.pebble-sdk/ && \
    touch /home/pebble/.pebble-sdk/NO_TRACKING \
    "

WORKDIR /pebble
VOLUME /pebble

CMD /bin/bash
