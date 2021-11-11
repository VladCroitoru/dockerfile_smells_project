FROM node:6.6.0-wheezy

MAINTAINER Maximilian Friedmann
RUN apt-get update && apt-get install -y xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic x11-apps clang libdbus-1-dev libgtk2.0-0 libnotify-dev libgnome-keyring-dev libasound2 libcap-dev libcups2 libxtst-dev libxss1 libnss3 gcc-multilib g++-multilib libgconf-2-4 libxtst6 libgtk2.0-0 

RUN useradd -ms /bin/bash node -G sudo
RUN chown -R node:node /home/node
RUN echo %sudo ALL=NOPASSWD: ALL >> /etc/sudoers
WORKDIR /home/node
ENV HOME /home/node
USER node

# Create app directory
RUN mkdir -p /home/node/app
WORKDIR /home/node/app

# Install app dependencies
COPY package.json /home/node/app/
RUN npm install

# Bundle app source
COPY . /home/node/app

EXPOSE 8080
# CMD DEBUG=nightmare:*,electron:* xvfb-run --server-args="-screen 0 1024x768x24" npm start -s hn -m create -p 11878025
CMD xvfb-run --server-args="-screen 0 3840x2160x24" npm start -s hn -m create -p 11878025