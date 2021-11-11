############################################################
# Dockerfile to build a container that maps files using KN
############################################################

# Set the base image to python v3
FROM python:3.4-slim

# File Author / Maintainer
MAINTAINER Charles Blatti <blatti@illinois.edu>

# Update the repository sources list
RUN apt-get update && apt-get install -y \
    curl \
    time \
    rsync \
    wget \
    s3cmd \
    python3-pip

RUN pip3 install redis
COPY src/kn_mapper.py /home/src/kn_mapper.py
COPY sample_props.txt /home/
COPY sample_genes.txt /home/

# Set default contain command on run
CMD /bin/bash

# Set container execution behavior
# ENTRYPOINT
