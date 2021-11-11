FROM ubuntu

# set labels
LABEL maintainer="Nightah"

# environment variables
ENV DEBIAN_FRONTEND="noninteractive" \
HOME="/build" \
TERM="xterm"

RUN \
  apt-get update && \
  apt-get dist-upgrade -y && \
  apt-get install ca-certificates curl git gpg ssh sudo wget -y

RUN \
  echo "**** Add build user ****" && \
    useradd -m -s /bin/bash -d /build build && \
  echo "**** Install Authelia CD pre-requisites ****" && \
    update-ca-certificates -f && \
    wget -qO - 'https://proget.hunterwittenborn.com/debian-feeds/makedeb.pub' | gpg --dearmor | tee /usr/share/keyrings/makedeb-archive-keyring.gpg > /dev/null && \
    echo 'deb [signed-by=/usr/share/keyrings/makedeb-archive-keyring.gpg arch=all] https://proget.hunterwittenborn.com/ makedeb main' | tee /etc/apt/sources.list.d/makedeb.list && \
    apt-get update && \
    apt-get install makedeb -y

# set default user
USER build