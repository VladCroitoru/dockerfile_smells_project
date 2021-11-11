FROM  dartainers/dart-runtime:latest
MAINTAINER  Anatoly Pulyaevskiy <anatoly.pulyaevskiy@gmail.com>

LABEL Description="Docker image with Dart runtime and Content Shell"

ENV DEBIAN_FRONTEND noninteractive
ENV CHANNEL stable
ENV SDK_VERSION 1.19.1
ENV ARCHIVE_URL https://storage.googleapis.com/dart-archive/channels/$CHANNEL/release/$SDK_VERSION

RUN echo 'deb http://archive.ubuntu.com/ubuntu/ precise multiverse' >> /etc/apt/sources.list
RUN echo 'deb-src http://archive.ubuntu.com/ubuntu/ precise multiverse' >> /etc/apt/sources.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu/ precise-updates multiverse' >> /etc/apt/sources.list
RUN echo 'deb-src http://archive.ubuntu.com/ubuntu/ precise-updates multiverse' >> /etc/apt/sources.list
RUN apt-get update

RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections
RUN apt-get install --no-install-recommends -y -q chromium-browser libudev0 \
  ttf-kochi-gothic ttf-kochi-mincho ttf-mscorefonts-installer ttf-indic-fonts \
  ttf-dejavu-core ttf-indic-fonts-core fonts-thai-tlwg msttcorefonts xvfb

WORKDIR /usr/local/content_shell

RUN curl $ARCHIVE_URL/dartium/content_shell-linux-x64-release.zip > content_shell.zip
RUN unzip content_shell.zip > /dev/null
RUN rm content_shell.zip

ENV PATH /usr/local/content_shell/drt-lucid64-full-$CHANNEL-$SDK_VERSION.0:$PATH
ENV DISPLAY :99.0

WORKDIR /root
