FROM phusion/baseimage:0.9.13
MAINTAINER Michael Williams
ENV REFRESHED_AT 2016-03-23

# Set correct environment variables.
ENV ERLANG_MAJOR 18
ENV ERLANG_VERSION 18.3

# ENV HOME does not seem to work currently; HOME is unset in Docker container.
# See discussion at: https://github.com/phusion/baseimage-docker/issues/119
RUN echo /root > /etc/container_environment/HOME

# Disable SSH.
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use phusion/baseimage's init system.
CMD ["/sbin/my_init"]

# Set the locale.
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# See discussion at: https://github.com/phusion/baseimage-docker/issues/58
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install dependencies and useful tools.
RUN apt-get update \
  && apt-get install -y autoconf build-essential libssl-dev libncurses5-dev \
  && apt-get install -y git

# Build Erlang from source and install it.
RUN mkdir -p /usr/src/erlang \
  && git clone --branch OTP-18.3 --depth 1 https://github.com/erlang/otp.git /usr/src/erlang \
  && cd /usr/src/erlang \
  && export ERL_TOP=$PWD \
  && export PATH=$ERL_TOP/bin:$PATH \
  && ./otp_build autoconf \
  && ./configure \
  && make \
  && make install \
  && rm -r /usr/src/erlang

# Clean up.
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
