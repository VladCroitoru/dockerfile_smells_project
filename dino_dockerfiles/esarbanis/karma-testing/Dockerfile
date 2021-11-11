FROM node:latest
MAINTAINER Efthymios Sarmpanis <e.sarbanis@gmail.com>

# Install Firefox
RUN apt-get -y update
RUN apt-get install -y -q software-properties-common wget
RUN add-apt-repository -y ppa:mozillateam/firefox-next
RUN apt-get update -y
RUN apt-get install -y -q firefox openjdk-8-jre-headless xvfb chromium

# Install Chrome
ADD xvfb-chromium /usr/bin/xvfb-chromium
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser


CMD ["node"]
