FROM debian:stretch-slim

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# runtime dependencies
RUN apt-get update
RUN apt-get install -y apt-transport-https ca-certificates
RUN apt-get install -y git wget curl tar
RUN apt-get install -y python python-dev python-virtualenv python-pip
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" > /etc/apt/sources.list.d/ansible.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
RUN apt-get update
RUN apt-get install -y ansible
RUN mkdir /opt/projects/ && mkdir /opt/projects/tmp && mkdir /var/www/
RUN pip install docker-py

WORKDIR /opt/projects/
