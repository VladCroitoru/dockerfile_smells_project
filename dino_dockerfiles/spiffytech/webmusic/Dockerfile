FROM risingstack/alpine:3.3-v6.2.0-3.6.0

RUN apk update && apk add ffmpeg python-dev make g++

RUN mkdir /source
WORKDIR /source
COPY build .
COPY out/* ./
COPY package.json ./package.json
RUN npm install

CMD ["node", "server.js"]
