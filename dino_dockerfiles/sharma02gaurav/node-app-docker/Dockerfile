FROM node:6.11.0

RUN mkdir -p /usr/src/node-app
WORKDIR /usr/src/node-app

COPY package.json /usr/src/node-app
RUN npm install

COPY . /usr/src/node-app

EXPOSE 4300

CMD [ "npm", "start" ]