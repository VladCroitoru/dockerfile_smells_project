FROM node:latest

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json .
COPY package.json package-lock.json ./

# Fixes mdns build error; see https://github.com/nodejs/docker-node/issues/10
RUN apt-get update && apt-get --yes install libavahi-compat-libdnssd-dev

RUN npm install

# Bundle app source
COPY . .

CMD [ "npm", "start" ]
