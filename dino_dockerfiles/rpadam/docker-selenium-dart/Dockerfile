
FROM selenium/standalone-chrome-debug:3.11.0

MAINTAINER Raphael Adam <raphael.adam@workiva.com, raphael912003@gmail.com>

LABEL Description="This image contains: Selenium-HQ with Chrome; the Dart SDK; and Sauce Connect"

USER root

ENV CHANNEL stable
ENV SDK_VERSION latest
ENV ARCHIVE_URL https://storage.googleapis.com/dart-archive/channels/$CHANNEL/release/$SDK_VERSION
ENV SC_VERSION 4.4.6
ENV PATH $PATH:/usr/lib/dart/bin

RUN apt-get update && apt-get install -y \
    git \
    ssh \
    unzip \
    wget \
    curl \
    imagemagick \
    libmagick++-dev \
    ffmpeg \
    xvfb \
    openjdk-8-jre-headless \
    make \
    automake \
    g++ \
    libpoppler-glib-dev \
    poppler-utils \
    wxgtk3.0-dev \
  && apt-get clean

RUN wget -O ./sauce-connect.tar.gz https://saucelabs.com/downloads/sc-$SC_VERSION-linux.tar.gz \
  && tar -zxvf sauce-connect.tar.gz \
  && mv sc-$SC_VERSION-linux/bin/sc /usr/local/bin/ \
  && rm -rf sauce-connect.tar.gz \
  && rm -rf sc-$SC_VERSION-linux/

RUN wget $ARCHIVE_URL/sdk/dartsdk-linux-x64-release.zip \
  && unzip dartsdk-linux-x64-release.zip \
  && cp dart-sdk/* /usr/local -r \
  && rm -rf dartsdk-linux-x64-release.zip

RUN git clone https://github.com/vslavik/diff-pdf.git \
  && cd diff-pdf/ \
  && ./bootstrap \
  && ./configure \
  && make \
  && make install
