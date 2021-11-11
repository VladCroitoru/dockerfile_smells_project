FROM ubuntu:precise
MAINTAINER Joel Wurtz <jwurtz@jolicode.com>

#ENV HOME /home
#ENV USER1 gitlab_ci_runner
# Add apt repository needed
RUN echo 'deb http://archive.ubuntu.com/ubuntu precise main universe' > /etc/apt/sources.list  && \
    echo 'deb http://archive.ubuntu.com/ubuntu precise-security main universe' >> /etc/apt/sources.list && \
    echo 'deb http://archive.ubuntu.com/ubuntu precise-updates main universe' >> /etc/apt/sources.list && \
    echo 'deb http://archive.ubuntu.com/ubuntu precise-backports main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb-src http://archive.ubuntu.com/ubuntu precise main universe' >> /etc/apt/sources.list && \
    echo 'deb-src http://archive.ubuntu.com/ubuntu precise-security main universe' >> /etc/apt/sources.list && \
    echo 'deb-src http://archive.ubuntu.com/ubuntu precise-updates main universe' >> /etc/apt/sources.list && \
    echo 'deb-src http://archive.ubuntu.com/ubuntu precise-backports main restricted universe multiverse' >> /etc/apt/sources.list && \
    mkdir -p $HOME && \
    apt-get update && \
    apt-get install -y python-software-properties git curl wget sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# ADD $USER1 User
#RUN addgroup --gid=1000 $USER1 && \
#    adduser --system --uid=1000 --home /home --shell /bin/bash $USER1 && \
#    echo "$USER1 ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
#    chown -R $USER1:$USER1 /home && \
#    chown -R $USER1:$USER1 /usr/local

#USER $USER1
