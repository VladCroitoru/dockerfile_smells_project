FROM ubuntu:14.04

MAINTAINER Erik Osterman "e@osterman.com"

# System ENV
ENV TIMEZONE Etc/UTC
ENV DEBIAN_FRONTEND noninteractive
ENV PATH "$PATH:/armada:/usr/local/bin"
ENV TERM xterm

ENV DOCKER_GID 233
ENV DOCKER_HOST=

# Locale specific
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Git 
ENV GIT_USER_GROUPS docker
ENV GIT_USERS=
ENV GITHUB_USERS= 

USER root

#    (curl -sSL https://get.docker.com/ | sh) && \ 

RUN apt-get update && \
    apt-get install -y \
                    locales \
                    realpath \
                    openssh-server \
                    curl \
                    git \
                    vim && \
    mkdir -p /var/run/sshd && \
    sed -i 's:session\s*required\s*pam_loginuid.so:session optional pam_loginuid.so:g' /etc/pam.d/sshd && \
    ([ -f /etc/ssh/ssh_host_rsa_key ] || ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key)  && \
    locale-gen $LANGUAGE && \
    dpkg-reconfigure locales && \
    echo "$TIMEZONE" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    ln -s /home/docker /var/lib/docker && \
    groupadd -g $DOCKER_GID docker

ADD app/ /armada
ADD start /start

EXPOSE 22

ENTRYPOINT ["/start"]


