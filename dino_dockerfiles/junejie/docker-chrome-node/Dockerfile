FROM node:stretch

RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive"
RUN apt-get install -y libgconf-2-4 openjdk-8-jre-headless
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update -y
RUN apt-get install google-chrome-stable -y
ENV CHROME_BIN /usr/bin/google-chrome
