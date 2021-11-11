#
# Base Dockerfile
#
#
FROM hpierce/docker-ubuntu-16.04-base-java7

MAINTAINER Hugh Pierce

ENV DEBIAN_FRONTEND noninteractive
ENV RUNDECK_VERSION 2.6.9-1

# required packages for ansible
RUN apt-get install -y python python-pip python-openssl

# install ansible
RUN pip install --upgrade pip && pip install ansible

# rundeck install
ADD http://dl.bintray.com/rundeck/rundeck-deb/rundeck-${RUNDECK_VERSION}-GA.deb /tmp/rundeck.deb
RUN dpkg -i /tmp/rundeck.deb && rm /tmp/rundeck.deb
ADD https://github.com/Batix/rundeck-ansible-plugin/releases/download/2.0.0/ansible-plugin-2.0.0.jar /var/lib/rundeck/libext/
RUN chown 644 /var/lib/rundeck/libext/ansible-plugin-2.0.0.jar

# Add keys
ADD .ssh /var/lib/rundeck/.ssh 

# Ansible configuration files
ADD ansible /etc/ansible

RUN chown -R rundeck:rundeck /var/lib/rundeck

# ports
EXPOSE 4440 4443

ENTRYPOINT /etc/init.d/rundeckd start && /bin/bash

