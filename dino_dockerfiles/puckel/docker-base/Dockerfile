# VERSION 1.0
# AUTHOR: Matthieu "Puckel_" Roisil
# DESCRIPTION: Simple Debian image based on debian:latest
# BUILD: docker build --rm -t puckel/docker-base .
# SOURCE: https://github.com/puckel/docker-base

FROM debian:latest
MAINTAINER Puckel_

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
# Work around initramfs-tools running on kernel 'upgrade': <http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>
ENV INITRD No

RUN echo "APT::Install-Recommends \"false\"; APT::Install-Suggests \"false\";" | tee -a  /etc/apt/apt.conf \
    && apt-get update -yqq \
    && apt-get install -yqq \
    psmisc \
    procps \
    net-tools \
    cron \
    curl \
    locales \
    vim \
    ca-certificates \
    && apt-get clean \
    && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base

# Define en_US.
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Define default workdir
WORKDIR /root
