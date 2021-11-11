# -*- shell-script -*-
FROM debian:jessie
MAINTAINER Guido Classen <clagix@gmail.com>

LABEL description="Automated Build for SWARCO Embedded Linux V2 operating system"

#ENV DEBIAN_FRONTEND noninteractive

RUN useradd -ms /bin/bash builduser &&                  \
    apt-get --yes update &&                             \
    apt-get --yes --no-install-recommends install       \
            autoconf                                    \
            automake                                    \
            bison                                       \
            bzip2                                       \
            ca-certificates                             \
            cpp                                         \
            curl                                        \
            flex                                        \
            g++                                         \
            gcc                                         \
            gettext                                     \
            git                                         \
            groff-base                                  \
            kmod                                        \
            libc6-dev                                   \
            liblzo2-2                                   \
            liblzo2-dev                                 \
            libncurses5-dev                             \
            libz-dev                                    \
            make                                        \
            net-tools                                   \
            patch                                       \
            perl                                        \
            perl-modules                                \
            texinfo                                     \
            xz-utils                                    \
            cmake                                       \
            uuid-dev                                    \
            &&                                          \
    apt-get clean &&                                    \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


COPY docker_build.sh /home/builduser
#USER builduser
WORKDIR /home/builduser

RUN ./docker_build.sh

#USER root
