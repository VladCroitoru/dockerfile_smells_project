FROM node:7.5.0-alpine
WORKDIR /hubot
COPY package.json /hubot
RUN npm install
COPY . /hubot
CMD ["npm", "start"]
