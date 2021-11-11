# imapfilter
# Use phusion/baseimage as base image. To make your builds
# reproducible, make sure you lock down to a specific version, not
# to `latest`! See
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md
# for a list of version numbers.
FROM phusion/baseimage

MAINTAINER Person Sebastien <personseb@yahoo.fr>

# Set correct environment variables.
#ENV HOME /root
### not longer needed in baseimage 0.9.17 (release date: 2015-07-15)

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
#RUN /etc/my_init.d/00_regen_ssh_host_keys.sh
#The following was part of ka2er's Dockerfile, I commented it out
#RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# no need for confirmation
ENV DEBIAN_FRONTEND noninteractive

# Recommends are as of now still abused in many packages
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/no-recommends
RUN echo "APT::Get::Assume-Yes "true";" > /etc/apt/apt.conf.d/always-yes

# ...put your own build instructions here...
RUN apt-get -qq update
RUN apt-get -y install git-core lua5.2 libpcre3 libssl1.0.0 liblua5.2

WORKDIR /home/imapfilter

RUN git clone https://github.com/lefcha/imapfilter.git .

# dev dependancies
RUN apt-get -y install build-essential libpcre3-dev libssl-dev liblua5.2-dev

# patch src for debian/ubuntu support
RUN sed -i "s/-llua/-llua5.2/g" src/Makefile
RUN sed -i "s|#include <lua|#include <lua5.2/lua|g" src/*[ch]
RUN sed -i "s|#include <lauxlib|#include <lua5.2/lauxlib|g" src/*[ch]

RUN make all
RUN make install

# Clean up APT when done.
RUN apt-get autoremove --purge build-essential libpcre3-dev libssl-dev liblua5.2-dev
RUN apt-get autoremove --purge
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /etc/service/imapfilter
ADD imapfilter.sh /etc/service/imapfilter/run

VOLUME /root/.imapfilter
