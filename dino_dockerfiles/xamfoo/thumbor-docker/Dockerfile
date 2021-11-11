FROM phusion/baseimage:0.9.16
MAINTAINER xamfoo

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

ADD setup /setup
RUN DEBIAN_FRONTEND=noninteractive \
  /setup/install.sh
