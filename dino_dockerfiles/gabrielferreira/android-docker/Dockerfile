FROM ubuntu:14.04

MAINTAINER Gabriel Ferreira "contato@gabrielferreira.com"

# Make sure the package repository is up to date.
RUN apt-get update && apt-get -y upgrade \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install a basic SSH server
RUN apt-get update && apt-get install -y openssh-server \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

# Add user jenkins to the image
RUN adduser --quiet jenkins
# Set password for the jenkins user (you may want to alter this).
RUN echo "jenkins:jenkins" | chpasswd
# Add jenkins user as sudo
RUN adduser jenkins sudo

# Install java7
RUN apt-get update && apt-get install -y software-properties-common \
  && add-apt-repository -y ppa:webupd8team/java \
  && apt-get update \
  && echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
  && apt-get install -y oracle-java7-installer \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Install Deps
RUN dpkg --add-architecture i386 \
  && apt-get update && apt-get install -y --force-yes \
  expect \
  git \
  wget \
  libc6-i386 \
  lib32stdc++6 \
  lib32gcc1 \
  lib32ncurses5 \
  lib32z1 \
  python \
  curl \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Install Android SDK
RUN cd /opt \
  && wget --output-document=android-sdk.tgz --quiet http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz \
  && tar xzf android-sdk.tgz \
  && rm -f android-sdk.tgz \
  && chown -R root.root android-sdk-linux

# Setup environment
ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

# Install sdk elements
COPY tools /opt/tools
ENV PATH ${PATH}:/opt/tools

#RUN while :; do echo 'y'; sleep 2; done | android update sdk --all --no-ui

RUN echo 'ANDROID_HOME="/opt/android-sdk-linux"' > /etc/environment
RUN echo 'PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/opt/android-sdk-linux/tools:/opt/android-sdk-linux/platform-tools:/opt/tools"' >> /etc/environment

RUN which adb
RUN which android

# Create emulator
#RUN echo "no" | android create avd \
#                --force \
#                --device "Nexus 5" \
#                --name test \
#                --target android-21 \
#                --abi armeabi-v7a \
#                --skin WVGA800 \
#                --sdcard 512M

# Cleaning
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# GO to workspace
RUN mkdir -p /opt/workspace
WORKDIR /opt/workspace
RUN chown -R jenkins:jenkins /opt/workspace
RUN chown -R jenkins:jenkins /opt/android-sdk-linux
VOLUME /opt/workspace

# Standard SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
