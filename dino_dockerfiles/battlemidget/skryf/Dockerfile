#
# Skryf
#
# https://github.com/skryf/Skryf

FROM ubuntu
MAINTAINER Adam Stokes <adamjs@cpan.org>

# locales
ENV DEBIAN_FRONTEND noninteractive
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales

RUN apt-get update
RUN apt-get upgrade -y

# Install basic packages.
RUN apt-get install -y curl git perl perl-modules cpanminus cpanoutdated build-essential

ENV HOME /root
WORKDIR /root

RUN cpanm --notest https://github.com/skryf/Skryf.git
RUN cpanm --notest https://github.com/skryf/Skryf-Theme-Booshka.git
