FROM node:7.9.0
RUN apt-get update -qq && apt-get install -y gconf-service libasound2 libatk1.0-0 libcups2 libdbus-1-3 libgconf-2-4 libgtk-3-0 libnspr4 libx11-xcb1 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome*.deb
RUN export CHROME_BIN=/usr/bin/google-chrome
