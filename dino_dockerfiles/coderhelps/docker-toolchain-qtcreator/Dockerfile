FROM ubuntu:latest
MAINTAINER Tim <tim@coderhelps.com>

# Install lots of packages
RUN apt-get update && apt-get build-dep qt5-default -y && apt-get install -y libxcb-xinerama0-dev build-essential perl python git "^libxcb.*" libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev flex bison gperf libicu-dev libxslt-dev ruby libssl-dev libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev libfontconfig1-dev libcap-dev libxtst-dev libpulse-dev libudev-dev libpci-dev libnss3-dev libasound2-dev libxss-dev libegl1-mesa-dev gperf bison libasound2-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev wget p7zip-full

WORKDIR /toolchain/qtcreator-4.0.3

RUN wget http://download.qt.io/official_releases/qtcreator/4.0/4.0.3/installer_source/linux_gcc_64_rhel66/qtcreator.7z

RUN 7z x qtcreator.7z

VOLUME ['/toolchain/qtcreator-4.0.3']
