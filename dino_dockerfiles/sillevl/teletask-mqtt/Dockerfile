FROM node:alpine
MAINTAINER Sille Van Landschoot <info@sillevl.be>

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install

# Bundle app source
COPY . /usr/src/app

VOLUME /config

CMD [ "npm", "start" , "--", "--config", "/config/settings.json"]
