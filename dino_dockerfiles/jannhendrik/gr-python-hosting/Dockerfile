#
# Python Dockerfile
#
# https://github.com/dockerfile/python
#

# Pull base image.
FROM ubuntu:16.04

# Install Python.
RUN \
  apt-get update && \
  apt-get install --no-install-suggests -y python3 python3-dev python3-pip python3-virtualenv && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Install numpy
RUN \
  pip3 install numpy
# Install treelib
RUN \
  pip3 install treelib
# Install web.py
RUN \
  pip3 install web.py==0.40.dev0
