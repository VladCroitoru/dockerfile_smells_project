FROM        ubuntu:12.04
MAINTAINER  George Ornbo "george@shapeshed.com"

# Update apt sources
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

# Update the package repository
 RUN apt-get update; apt-get upgrade -y; apt-get install locales

# Configure timezone and locale
RUN echo "Europe/London" > /etc/timezone; dpkg-reconfigure -f noninteractive tzdata
RUN export LANGUAGE=en_US.UTF-8; export LANG=en_US.UTF-8; export LC_ALL=en_US.UTF-8; locale-gen en_US.UTF-8; DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

# Install base system
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget curl python-software-properties python g++ make
RUN add-apt-repository ppa:chris-lea/node.js
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs

ADD start.sh /start.sh
RUN chmod 0755 /start.sh
CMD ["bash", "start.sh"]
