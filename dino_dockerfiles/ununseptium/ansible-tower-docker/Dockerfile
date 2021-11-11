#ansible-tower dockerfile
# WORK IN PROGRESS
# DO NOT USE IN PRODUCTION
FROM ubuntu:trusty

MAINTAINER tim@arctium.io

ENV TOWER_VER 3.0.3
    
# Enable EPEL-Repo, install Ansible
RUN apt-get update -y \
    && apt-get install software-properties-common curl -y \
    && apt-add-repository ppa:ansible/ansible \
    && apt-get install ansible -y

# Download and install Tower
RUN cd /opt \
    && curl -O http://releases.ansible.com/ansible-tower/setup/ansible-tower-setup-${TOWER_VER}.tar.gz \
    && tar xvzf ansible-tower-setup-${TOWER_VER}.tar.gz \
    && cd ansible-tower-setup-${TOWER_VER}
    
ADD inventory /opt/ansible-tower-setup-${TOWER_VER}/inventory

RUN cd /opt/ansible-tower-setup-${TOWER_VER} \
    && sudo ./setup.sh

EXPOSE 443 8080
