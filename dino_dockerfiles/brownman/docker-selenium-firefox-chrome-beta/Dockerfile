FROM ubuntu:trusty
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

MAINTAINER Chris Nelosn <cnelson@cnelson.org>
RUN apt-get -y update
RUN apt-get update -y
RUN apt-get install -y -q \
  openjdk-7-jre-headless \
  x11vnc \
  xvfb \
  xfonts-100dpi \
  xfonts-75dpi \
  xfonts-scalable \
  xfonts-cyrillic \
  libgtk2.0-0 \
  libdbus-glib-1-2 \
  libasound2

EXPOSE 4444 5999
ENTRYPOINT ["/app/entry_point.sh"]
CMD ["-singleWindow", "-trustAllSSLCertificates"]

ADD https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/32.0/linux-x86_64/en-US/firefox-32.0.tar.bz2 /tmp/firefox-32.0.tar.bz2
ADD http://selenium-release.storage.googleapis.com/2.44/selenium-server-standalone-2.44.0.jar /opt/selenium/selenium-server-standalone-2.44.0.jar
ADD ./scripts/ /app

RUN mkdir -p /opt && tar -C /opt -xjf /tmp/firefox-32.0.tar.bz2

