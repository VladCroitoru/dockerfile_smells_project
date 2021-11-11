FROM node:latest
MAINTAINER SushiFu

# Create app directory
RUN mkdir -p /app
WORKDIR /app

# Bundle app source
COPY . /app

RUN npm install

VOLUME /docker

CMD [ "node", "index.js", "/docker" ]
