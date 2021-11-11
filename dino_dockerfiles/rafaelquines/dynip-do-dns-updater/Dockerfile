FROM node:alpine

LABEL maintainer="rafaelquines@gmail.com"

# Create app directory
RUN mkdir -p /app
WORKDIR /app

# Install app dependencies
COPY package.json /app
RUN npm install

# Bundle app source
COPY ./dist /app

CMD [ "npm", "start" ]