FROM iojs:1-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

EXPOSE 8080
CMD [ "npm", "start" ]

COPY package.json /usr/src/app/
RUN npm install

COPY . /usr/src/app
RUN ./node_modules/.bin/grunt build

