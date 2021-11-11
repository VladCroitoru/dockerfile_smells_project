FROM node:12-buster-slim as base
RUN apt-get -y update && apt-get install -y ffmpeg python3 make gcc g++ opus-tools cmake sox git wget 
WORKDIR /app
COPY . /app
RUN npm install -g node-gyp
RUN npm install
RUN mkdir /app/models
RUN wget -O /app/models/deepspeech-0.9.3-models.pbmm https://github.com/khlam/musicbot/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
CMD node main.js