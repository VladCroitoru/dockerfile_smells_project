FROM node:6

RUN apt-get update -y
RUN apt-get install -y ca-certificates apt-transport-https ttf-wqy-zenhei ttf-unfonts-core
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update -y
RUN apt-get install -y google-chrome-unstable
RUN useradd headless --shell /bin/bash --create-home
RUN usermod -a -G sudo headless
RUN echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers
RUN echo 'headless:nopassword' | chpasswd
RUN mkdir /data

USER headless
