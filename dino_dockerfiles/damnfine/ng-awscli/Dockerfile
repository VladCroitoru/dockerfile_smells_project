FROM node:10.21
# update and upgrade packages
RUN apt-get update -yq && apt-get upgrade -yq

# Install GIT
RUN apt-get install -yq bash git openssh-server

# Install Python
RUN apt-get install -yq python-pip python-dev build-essential

# Install AWS CLI
RUN pip install --upgrade pip
RUN pip install awscli --user --upgrade
# Tidy up
# TODO
# Add CLI to PATH
ENV PATH "$PATH:~/.local/bin"

# Install Angular CLI
RUN yarn global add @angular/cli@9.1.11

ENV CHROME_PATH=/usr/bin/chromium-browser \
  CHROME_BIN=/usr/bin/chromium-browser

# Install Chromium and dependencies
RUN \
  apt-get install -yq chromium gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 \
  libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 \
  libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 \
  libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 \
  ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget

# Tidy up
# TODO