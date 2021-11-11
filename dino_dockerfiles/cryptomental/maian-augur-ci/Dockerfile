# Docker Image with MAIAN and Solc for Augur contracts security analysis

# Pull base image
FROM ubuntu:16.04

# Install Python and build tools
RUN \
  apt-get update && \
  apt-get install -y build-essential software-properties-common libssl-dev wget && \
  apt-get install -y python python-dev python-pip git psmisc lsof

# Install Solidity compiler 0.4.20 release
RUN wget https://github.com/ethereum/solidity/releases/download/v0.4.20/solc-static-linux && \
  mv solc-static-linux /usr/bin/solc

# Install Go Ethereum (GETH) from Ethereum PPA
RUN \
  add-apt-repository ppa:ethereum/ethereum && \
  apt-get update && \
  apt-get -y install ethereum

# Install MAIAN from GitHub
RUN \
  git clone https://github.com/MAIAN-tool/MAIAN.git

# Install Python dependencies

RUN pip install --upgrade pip

COPY requirements.txt scripts/requirements.txt
RUN \
  pip install -r scripts/requirements.txt

# Copy test runner script to Docker image
COPY scripts/test_runner.py scripts/test_runner.py

# Set SOLC environment variable
ENV SOLC /usr/bin/solc

# Add exec rights to solc
RUN chmod +x /usr/bin/solc
