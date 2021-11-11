# # #
# Base Dockerfile for Elixir applications
# # #

FROM ubuntu:trusty
MAINTAINER Jan Lelis <mail@janlelis.de>
ENV DEBIAN_FRONTEND noninteractive

# Ensure locale
RUN apt-get -y update
RUN dpkg-reconfigure locales && \
  locale-gen en_US.UTF-8 && \
  /usr/sbin/update-locale LANG=en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Essential packages
RUN apt-get -y update
RUN apt-get -y install wget build-essential git

# Install Erlang
RUN mkdir /tmp/erlang-build
WORKDIR /tmp/erlang-build
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
RUN dpkg -i erlang-solutions_1.0_all.deb
RUN apt-get -y update
RUN apt-get -y install erlang

# Build Elixir
RUN git clone https://github.com/elixir-lang/elixir.git /tmp/elixir-source
WORKDIR /tmp/elixir-source
RUN git checkout v1.1.1
RUN make install

# Clean Up
WORKDIR /
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
