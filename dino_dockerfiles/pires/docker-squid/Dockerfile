FROM ubuntu:14.04

# Me, Myself and I
MAINTAINER Paulo Pires <pjpires@gmail.com>

# Install squid
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y dist-upgrade && \
  apt-get -y install squid3 runit

# Add configuration files
ADD squid.conf /etc/squid3/squid.conf

# Add runnable scripts
ADD run_squid.sh /etc/service/squid/run
RUN chmod u+x /etc/service/squid/run

CMD ["/usr/bin/runsvdir", "-P", "/etc/service"]