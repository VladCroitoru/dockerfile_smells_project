FROM node:alpine

# Create app directory
RUN mkdir -p /usr/src/pinguin
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/pinguin/
RUN npm install webpack -g
RUN npm install

# Bundle app source
COPY . /usr/src/pinguin

EXPOSE 8000
CMD [ "npm", "start" ]