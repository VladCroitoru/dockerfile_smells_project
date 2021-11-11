# Dart SDK with content_shell and xvfb

FROM rpadam/dart_docker:latest

MAINTAINER Raphael Adam <raphael.adam@workiva.com, raphael912003@gmail.com>

LABEL Description="This image contains the Dart SDK with content_shell and xvfb"

RUN echo "deb http://us.archive.ubuntu.com/ubuntu precise main multiverse" >> /etc/apt/sources.list \
    && apt-get update; echo 'true' && apt-get install -y \
    wget \
    unzip \
    xvfb \
    chromium-browser \
    libudev0 \
    && apt-get clean

# Install Content Shell
RUN wget $ARCHIVE_URL/dartium/content_shell-linux-x64-release.zip \
    && unzip content_shell-linux-x64-release.zip \
    && rm content_shell-linux-x64-release.zip
ENV PATH /drt-lucid64-full-$CHANNEL-$SDK_VERSION.0:$PATH
