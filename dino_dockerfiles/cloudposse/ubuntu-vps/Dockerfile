FROM ubuntu:14.04
MAINTAINER Erik Osterman "e@osterman.com"

# VPS Setup
ENV VPS_GITHUB_USERS=
ENV VPS_USER=
ENV VPS_GROUP $VPS_USER
ENV VPS_PASSWORD=
ENV VPS_ENABLE_SUDO true

# System ENV
ENV TIMEZONE Etc/UTC
ENV DEBIAN_FRONTEND noninteractive
ENV PATH "$PATH:/opt/bin:/usr/local/bin"
ENV TERM xterm
ENV PERL_MM_USE_DEFAULT true

USER root

# FIXME I should really make a more minimal vps instance and inherit from it =)

RUN apt-get update && \
    apt-get install -y \
                    software-properties-common \
                    locales \
                    openssh-server \
                    mosh \
                    curl \
                    git \
                    vim \
                    ruby \
                    make \
                    m4 \
                    unzip \
                    pssh \
                    screen \
                    s3cmd \
                    mysql-client \
                    bc \
                    nodejs \
                    npm \
                    whois \
                    dnsutils \
                    traceroute \
                    telnet \
                    mtr \
                    bundler \
                    libxml2 \
                    libxml2-dev \
                    libz-dev \
                    libexpat-dev \
                    perl-doc \
                    groff \
                    python-pip \
                    python-requests \
                    yui-compressor \
                    && \
    apt-add-repository multiverse && \
    add-apt-repository ppa:mc3man/trusty-media && \
    apt-get update && \
    apt-get -y install ffmpeg gstreamer0.10-ffmpeg imagemagick && \
    apt-get clean && \
    ln -s /lib/x86_64-linux-gnu/libdevmapper.so.1.02.1 /lib/x86_64-linux-gnu/libdevmapper.so.1.0 && \
    ln -s /lib/x86_64-linux-gnu/libdevmapper.so.1.02.1 /lib/x86_64-linux-gnu/libdevmapper.so.1.02 && \
    ln -s /usr/bin/nodejs /usr/bin/node && \
    npm install jslint jshint uglifyjs mincss -g && \
    mkdir -p /var/run/sshd && \
    mkdir -p /usr/local/bin && \
     echo '%sudo ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/vps && \
    sed -i 's:session\s*required\s*pam_loginuid.so:session optional pam_loginuid.so:g' /etc/pam.d/sshd && \
    ([ -f /etc/ssh/ssh_host_rsa_key ] || ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key)  && \
    mkdir -p /root/.ssh/ -m 0700 && \
    echo '\nHost github.com\n  StrictHostKeyChecking no\n  UserKnownHostsFile=/dev/null' >> /root/.ssh/config && \
    echo '\nHost gitlab.com\n  StrictHostKeyChecking no\n  UserKnownHostsFile=/dev/null' >> /root/.ssh/config 

# Locale specific
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN locale-gen $LANGUAGE && \
    dpkg-reconfigure locales && \
    echo "$TIMEZONE" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

ADD bin /opt/bin
ADD start /start
ADD env.sh /etc/profile.d/
ADD motd /etc/motd
ADD .vimrc /root/.vimrc
ADD .vimrc /etc/skel/.vimrc

EXPOSE 22

ENTRYPOINT ["/start"]

