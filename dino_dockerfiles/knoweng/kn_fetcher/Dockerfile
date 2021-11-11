############################################################
# Dockerfile to build a container that pulls KN subnetworks
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

RUN pip3 install awscli
RUN wget -O /home/credentials http://knowredis.knoweng.org:8085/s3reader.v2.creds
COPY kn_fetcher.sh /home/
RUN chmod 775 /home/kn_fetcher.sh


# Set default contain command on run
CMD /bin/bash

# Set container execution behavior
# ENTRYPOINT
