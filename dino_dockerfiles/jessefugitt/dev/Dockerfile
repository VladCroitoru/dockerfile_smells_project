# dev
#
# VERSION               0.0.1

FROM ubuntu:14.04
MAINTAINER Jesse Fugitt
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    lib32ncurses5 libgtk2.0-0 libgconf-2-4 libnss3 libasound2 libxtst6 \
    openssh-server \
    python-setuptools \
    software-properties-common \
    unzip \
 && /usr/bin/easy_install supervisor \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* 

#VSCode
RUN mkdir -p /tools \
 && wget -O /tools/VSCode-linux-x64-stable.zip https://az764295.vo.msecnd.net/stable/db71ac615ddf9f33b133ff2536f5d33a77d4774e/VSCode-linux-x64-stable.zip \
 && cd /tools \
 && unzip VSCode-linux-x64-stable.zip

# Java
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Configure authorized_keys for SSH
RUN mkdir /var/run/sshd \
 && mkdir -p /root/.ssh \
 && touch -f /root/.ssh/host_authorized_keys \
 && chmod 700 /root/.ssh \
 && chmod 600 /root/.ssh/host_authorized_keys

# Configure sshd to block authentication via password
RUN sed -i.bak 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

ADD supervisord.conf /etc/supervisord.conf

EXPOSE 22

# Expecting host to map using -v ~/.ssh/authorized_keys:/root/.ssh/host_authorized_keys
CMD cp /root/.ssh/host_authorized_keys /root/.ssh/authorized_keys \
 && chown root:root /root/.ssh/authorized_keys \
 && chmod 600 /root/.ssh/authorized_keys \
 && /usr/local/bin/supervisord -n -c /etc/supervisord.conf
