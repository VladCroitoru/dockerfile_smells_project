FROM node:8.1.4

MAINTAINER Tim Officer "timothyofficer@gmail.com"

# download Google signing key for Linux
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# add Google Chrome to repository
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt-get update; \
    apt-get install default-jre -y; \
    apt-get install xvfb -y; \
    apt-get install google-chrome-stable -y;

ENV CHROME_BIN /usr/bin/google-chrome
