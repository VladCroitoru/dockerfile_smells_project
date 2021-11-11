FROM node:8.11.3

MAINTAINER Tim Brandin "tim.brandin@studiointeract.se"

RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get install --no-install-recommends -y -q sudo curl python build-essential git ca-certificates

# Install chrome for headless testing
## install manually all the missing libraries
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

## install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# install meteor
RUN curl -sL https://install.meteor.com | sh

# Install chimp (for testing)
RUN npm install chimp@0.51.1

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen &&     echo 'LANG="en_US.UTF-8"'>/etc/default/locale &&     dpkg-reconfigure --frontend=noninteractive locales &&     update-locale LANG=en_US.UTF-8
RUN export LANG=en_US.UTF-8

RUN adduser --disabled-password --gecos '' builder
RUN usermod -aG sudo builder
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Fixes issues with builds not going through on Bitbucket Pipeline due to
# issues reaching unicode.org.
RUN apt-get install unicode-data

USER builder
