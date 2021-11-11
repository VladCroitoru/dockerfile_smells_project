# -*- shell-script -*-
FROM debian:jessie
MAINTAINER Guido Classen <clagix@gmail.com>

LABEL description="Automated Build for SWARCO Embedded Linux V3 operating system"

# older Docker version don't understand "ARG"
ENV DEBIAN_FRONTEND noninteractive
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
            wget                                        \
            cpio                                        \
            python                                      \
            unzip                                       \
            rsync                                       \
            bc                                          \
            locales                                     \
            file                                        \
            uuid-dev                                    \
            &&                                          \
    apt-get clean &&                                    \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN ls -l /home
RUN ls -l /home/builduser
RUN cat /etc/passwd

#    locale-gen en_US.utf8 &&                           \
#    /usr/sbin/update-locale LANG=en_US.utf8 &&         \

# install locales support
# 2017-04-28 gc: C.UTF-8 currently not work for compiling buildroot

#  apt-get update -qq && apt-get install -y locales -qq && locale-gen en_US.utf8 en_us && dpkg-reconfigure locales && dpkg-reconfigure locales && locale-gen C.UTF-8 && /usr/sbin/update-locale LANG=C.UTF-8
# ENV LANG en_US.utf8
# ENV LANGUAGE en_US.utf8
# ENV LC_ALL en_US.utf8
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8


COPY docker_build.sh /home/builduser/
USER builduser

RUN ls -l /home/builduser
WORKDIR /home/builduser
RUN ./docker_build.sh

#reset DEBIAN_FRONTEND to default value
ENV DEBIAN_FRONTEND newt

#USER root
