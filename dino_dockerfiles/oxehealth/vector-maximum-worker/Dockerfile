FROM ubuntu:16.04

MAINTAINER ron.haskins@oxehealth.com

# install packages
RUN apt-get update && \
    apt-get -y install \
        sudo \
        g++ \
        make \
        cmake

COPY ./config/etc/sudoers /etc/sudoers

# create a build user & add build user to groups
RUN useradd -ms /bin/bash build && \
    usermod -a -G build build && \
    usermod -a -G adm build && \
    usermod -a -G sudo build

USER build