FROM ubuntu:15.04
MAINTAINER Petre Pătrașc <petre@dreamlabs.ro>
ENV REFRESHED_AT 2015-10-17 00:07

# Noninteractive installs
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    locale-gen en_US.UTF-8

# System environment setup
ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    HOME=/root \
    DEBIAN_FRONTEND=noninteractive

# Require packages
RUN apt-get update -y -qq &&  \
    apt-get upgrade -y -qq && \
    apt-get install -qq -y \
        vim \
        curl \
        software-properties-common \
        supervisor \
        netcat

# Add Supervisor configuration
ADD supervisor /etc/supervisor/

ADD commands /root/commands
WORKDIR /root
CMD ["/root/commands/init.sh"]
