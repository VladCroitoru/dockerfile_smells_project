FROM ubuntu:trusty

ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

MAINTAINER Jacek Migdal <jacek@migdal.pl>

RUN apt-get install -y -q software-properties-common wget
RUN add-apt-repository -y ppa:chris-lea/node.js
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list

RUN apt-get update -y

RUN apt-get install -y -q \
  firefox \
  google-chrome-stable \
  openjdk-7-jre-headless \
  nodejs \
  x11vnc \
  xvfb \
  xfonts-100dpi \
  xfonts-75dpi \
  xfonts-scalable \
  xfonts-cyrillic \
  xdotool \
  psmisc

RUN npm install -g \
  selenium-standalone@2.44.0-1 \
  phantomjs@1.9.13 \
  nightwatch@0.5.35

# Disable the SUID sandbox so that chrome can launch without being in a privileged container
# From: https://github.com/danielfrg/docker-selenium (MIT license)
RUN dpkg-divert --add --rename --divert /opt/google/chrome/google-chrome.real /opt/google/chrome/google-chrome
RUN echo "#!/bin/bash\nexec /opt/google/chrome/google-chrome.real --disable-setuid-sandbox \"\$@\"" > /opt/google/chrome/google-chrome
RUN chmod 755 /opt/google/chrome/google-chrome

RUN groupadd -g 1000 selenium
RUN useradd -d /home/selenium -u 1000 -g 1000 -m selenium
RUN mkdir -p /home/selenium/chrome
RUN chown -R selenium:selenium /home/selenium

RUN groupadd -g 1001 tests
RUN useradd -d /home/tests -u 1001 -g 1001 -m tests
ADD ./config/nightwatch/ /home/tests

ADD ./bin/ /home/root/bin

EXPOSE 4444 5555
ENTRYPOINT ["sh", "/home/root/bin/start.sh"]
