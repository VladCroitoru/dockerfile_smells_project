FROM ubuntu:16.04
MAINTAINER Martin Hlavac <info@mhlavac.net>

# All apt-gets, we have to install some first to get apt-add-repository command
RUN \
    apt-get update && apt-get upgrade -y && \
    apt-get install wget -y && \
    wget -O - https://repo.saltstack.com/apt/ubuntu/18.04/amd64/latest/SALTSTACK-GPG-KEY.pub | apt-key add - && \
    echo "deb http://repo.saltstack.com/apt/ubuntu/18.04/amd64/latest bionic main" > /etc/apt/sources.list.d/saltstack.list && \
    apt-get update && \
    apt-get install -y syslinux-common python-software-properties software-properties-common python-git salt-minion && \
    mkdir -p /srv && \
    apt-get remove wget -y && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/cache/* && \
    rm -rf /var/lib/log/*

CMD ["/bin/bash"]
