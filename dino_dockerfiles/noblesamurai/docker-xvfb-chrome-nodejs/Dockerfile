# Use phusion/baseimage as base image.
FROM phusion/baseimage:latest

# Use closest ubuntu mirrors (prepend necessary lines to sources.list).
ADD ubuntu-mirrors /tmp/ubuntu-mirrors
RUN cat /tmp/ubuntu-mirrors > /etc/apt/sources.list

# Google chrome apt keys.
RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
RUN sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list

# Install the OS packages we need.
RUN apt-get update && apt-get install -y \
  git \
  google-chrome-stable \
  nodejs \
  npm \
  openjdk-6-jre-headless \
  unzip \
  xfonts-100dpi \
  xfonts-75dpi \
  xfonts-cyrillic \
  xfonts-scalable \
  xvfb

RUN ln -s /usr/bin/nodejs /usr/bin/node

# Chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/2.13/chromedriver_linux64.zip && sudo unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/;

# vim: set et sw=2:
