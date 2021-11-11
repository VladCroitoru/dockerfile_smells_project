FROM debian:latest
#
#
#
MAINTAINER Haruki Yukawa

# Install packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install sudo kafkacat git maven default-jdk wget vim awscli && \
    rm -rf /var/lib/apt/lists/*

## Set a default user. Available via runtime flag `--user docker`
## Add user to 'staff' group, granting them write privileges to /usr/local/lib/R/site.library
## User should also have & own a home directory, but also be able to sudo
RUN useradd docker \
        && passwd -d docker \
        && mkdir /home/docker \
        && chown docker:docker /home/docker \
        && addgroup docker staff \
        && addgroup docker sudo \
	&& chsh -s /bin/bash docker \
        && true

# No-op. This Docker image is intended only for use as a parent image
CMD ["cat /dev/null"]
