#
# IPFS Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

ENV GO_IPFS_VERSION v0.10.0
ENV IPFS_PATH /srv/ipfs

# Update & install packages for go-callisto dep
RUN apt-get update && \
    apt-get install -y wget

# Get go-callisto from github
RUN mkdir /opt/go-ipfs && \
    cd /opt/go-ipfs && \
    wget https://dist.ipfs.io/go-ipfs/${GO_IPFS_VERSION}/go-ipfs_${GO_IPFS_VERSION}_linux-amd64.tar.gz -O ${GO_IPFS_VERSION}.tar.gz && \
    tar xf  ${GO_IPFS_VERSION}.tar.gz --strip-components=1

# Install ipfs
WORKDIR /opt/go-ipfs
RUN bash install.sh

EXPOSE 5001

#CMD ipfs $OPTIONS
