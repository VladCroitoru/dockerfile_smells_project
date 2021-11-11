# Base image
FROM node:10.12.0-alpine

# Create and set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# Environment variables
ENV NODE_VERSION 10.12.0

# Install and cache app dependencies
COPY package*.json ./
RUN apk update && \
    apk add --update git && \
    apk add --update openssh
RUN npm install

EXPOSE 80

# start app
CMD ["npm", "start"]