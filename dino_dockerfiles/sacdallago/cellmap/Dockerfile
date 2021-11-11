FROM node:boron

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle app source
COPY . /usr/src/app

# Use defaults or ENV file
RUN mv config.js.template config.js

RUN npm install

EXPOSE 3000

CMD [ "npm", "start" ]