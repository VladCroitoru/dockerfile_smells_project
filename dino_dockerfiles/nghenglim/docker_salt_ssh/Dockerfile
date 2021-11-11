#
# Salt Stack Salt ssh Container
#

FROM ubuntu:16.04
MAINTAINER Liam <nghenglim.github.io>

# Update System
RUN apt-get update && apt-get install -y wget ssh

# Install Salt

RUN wget -O - https://repo.saltstack.com/apt/ubuntu/16.04/amd64/archive/2017.7.2/SALTSTACK-GPG-KEY.pub | apt-key add -
RUN echo 'deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/archive/2017.7.2 xenial main' > /etc/apt/sources.list.d/saltstack.list
RUN apt-get update && apt-get install -y  salt-minion salt-ssh

# Run Command

CMD "/bin/bash"
