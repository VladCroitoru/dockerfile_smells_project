FROM nlknguyen/alpine-mpich

MAINTAINER Ezequiel M Gioia <@eze1981>

# change to root user
USER root

# Install packages
RUN apk add --no-cache --update \
  ca-certificates \
  openssl \
  curl

# Download, build, and install Repast HPC
RUN mkdir /tmp/repast-hpc-src
WORKDIR /tmp/repast-hpc-src
RUN wget https://github.com/Repast/repast.hpc/releases/download/v2.2.0/repast_hpc-2.2.0.tgz \
  && tar -xvzf repast_hpc-2.2.0.tgz

COPY install2.sh /tmp/repast-hpc-src/repast_hpc-2.2.0/MANUAL_INSTALL

# Install NetCDF
WORKDIR /tmp/repast-hpc-src/repast_hpc-2.2.0/MANUAL_INSTALL
RUN sh install2.sh netcdf

# Install Boost
WORKDIR /tmp/repast-hpc-src/repast_hpc-2.2.0/MANUAL_INSTALL
RUN sh install2.sh boost

# Install Repast HPC
WORKDIR /tmp/repast-hpc-src/repast_hpc-2.2.0/MANUAL_INSTALL
RUN sh install2.sh rhpc

# Clean up
WORKDIR /
RUN rm -rf /tmp/*

# Browse to project directory
WORKDIR /project

# Move examples into /project directory
RUN mv /root/sfw/repast_hpc-2.2.0/bin/ /project/examples/
