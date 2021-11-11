#
# securefs Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

# Update & install packages
RUN apt-get update && \
    apt-get install -y git fuse libfuse-dev make build-essential

# install securefs
RUN git clone https://github.com/netheril96/securefs.git && \
    cd securefs && \
    make securefs
