FROM node:6-wheezy

MAINTAINER Markus Kramer

RUN apt-get update
RUN apt-get install -y ffmpeg

RUN git clone --depth=1 https://github.com/gtrias/stretto.git
WORKDIR /stretto
RUN npm install --unsafe-perm

EXPOSE 2000
ENTRYPOINT ["node", "app.js"]

