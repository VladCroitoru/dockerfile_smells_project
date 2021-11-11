#
# Docker Image with Mythril and Solc for CI/CD of Ethereum Solidity Codes
#

# Pull base image
FROM ubuntu:16.04

# Install Python && Necessary build tools
RUN \
  apt-get update && \
  apt-get install -y build-essential software-properties-common libssl-dev && \
  apt-get install -y python3 python3-dev python3-pip && \
  rm -rf /var/lib/apt/lists/*

# Creating symmetric links to refer python3/pip3 as python/pip
RUN \
  ln -s /usr/bin/python3 /usr/bin/python && \
  ln -s /usr/bin/pip3 /usr/bin/pip

# Install Mythril
RUN \
  pip install mythril

# Install Solidity compiler
RUN \
  add-apt-repository ppa:ethereum/ethereum && \
  apt-get update && \
  apt-get -y install solc

# Create scripts directory to store the python script
RUN mkdir scripts

# Copy local python script to Docker image
COPY scripts/processor.py scripts/processor.py
