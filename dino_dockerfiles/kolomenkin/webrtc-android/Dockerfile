#FROM ubuntu:16.04
FROM debian:9

MAINTAINER Sergey Kolomenkin "kolomenkin@gmail.com"

# ==========================================
# This Dockerfile is intended for building
# WebRTC for Android (both x86 and arm)
# using Google's build system
# ==========================================

# Prevent warnings about TERM not set:
ENV TERM xterm

# ==========================================
# install Google's depot_tools

ENV PATH /opt/depot_tools:$PATH
# disable depot_tools self-update to increase build speed:
ENV DEPOT_TOOLS_UPDATE 0

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get -y install \
        curl \
        git \
        python \
        wget \
    && git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git /opt/depot_tools

# ==========================================
# Run install-build-deps.sh to install WebRTC dependencies

# NOTE: ttf-mscorefonts is installed during install-build-deps.sh and its installer needs some user interaction in Ubuntu 14.04 and 16.04

COPY dockerhelpers/install-build-deps.sh \
     dockerhelpers/install-build-deps-android.sh \
        /root/docker-setup/

RUN apt-get -y install \
        lsb-release \
        sudo \
    && echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections \
    && /root/docker-setup/install-build-deps-android.sh

# ==========================================
# install main package list for human and gn build

RUN apt-get update \
    && apt-get upgrade -y \
    \
    && echo "Installing optional packages (for human)..." \
    && apt-get -y install \
        mc \
    \
    && echo "Installing packages for gn build..." \
    && apt-get -y install \
        ccache \
        cpio \
    && echo "Remove unused packages, final updates..." \
    && apt-get autoremove \
    && git -C /opt/depot_tools pull

# ==========================================
# Final steps
# ==========================================

#RUN mkdir -p "/root/webrtc" \
#    && cd "/root/webrtc" \
#    && fetch --nohooks webrtc_android \
#    && echo y | gclient sync --delete_unversioned_trees --revision "src@refs/remotes/branch-heads/60"

WORKDIR /root
