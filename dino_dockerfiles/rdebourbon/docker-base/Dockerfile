FROM ubuntu:16.04
MAINTAINER rdebourbon@xpandata.net

ENV DEBIAN_FRONTEND="noninteractive" \
    TERM="xterm"

RUN sed -i "/^deb.*universe/ s/universe/universe multiverse/" /etc/apt/sources.list && \
    apt-get -q update && \
    apt-get -qy --force-yes dist-upgrade && \
    apt-get install -qy --force-yes \
        apt-transport-https \
        bzip2 \
        ca-certificates curl \
        dnsutils \
        fping \
        git \
        inetutils-ping \
        nano \
        openssl \
        openssh-server \
        procps psmisc python python-software-properties \
        rsync rsyslog \
        software-properties-common ssl-cert sudo supervisor \
        tar telnet tmux traceroute tree \
        wget whois \
        unrar unzip \
        vim \
        xz-utils \
        zsh && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/tmp/* && \
    rm -rf /tmp/*
