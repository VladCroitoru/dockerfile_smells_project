FROM node:alpine

# Create app directory
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm install --only=production

# Bundle app source
COPY ./server.js ./server.js

EXPOSE 8888

ENV NODE_ENV production

CMD [ "npm", "start" ]