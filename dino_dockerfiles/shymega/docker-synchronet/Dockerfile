####################
# Dockerfile for   #
# building a SBBS  #
# image for Docker #
####################

# Set base image
FROM debian:buster

# Set maintainer.
LABEL maintainer="Dom Rodriguez <shymega@shymega.org.uk>"

# Update aptitude and install packages
# Install packages.

RUN apt-get -yq update && \
  apt-get -yq install build-essential linux-libc-dev \
    libncurses5-dev libnspr4-dev libcap2-dev gdb sudo \
    unzip lrzsz gkermit \
    python pkgconf cvs perl \
    zip

# Create user
RUN useradd -rm -d /docker docker

# Set user
USER docker

# Move to sbbs dir
RUN mkdir -p /docker/sbbs
WORKDIR /docker/sbbs

# Add Makefile
ADD http://cvs.synchro.net/cgi-bin/viewcvs.cgi/*checkout*/install/GNUmakefile \
    /docker/sbbs/GNUmakefile

USER root
RUN chown -Rv docker: /docker
USER docker

# Compile
RUN make && make install

# Set entrypoint to SBBS
CMD ["/docker/sbbs/exec/sbbs"]
