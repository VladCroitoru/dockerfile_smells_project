FROM node:4.2
MAINTAINER Masato Shimizu <ma6ato@gmail.com>

RUN mkdir -p /app
WORKDIR /app

COPY package.json /app/
COPY bower.json /app/
COPY gulpfile.js /app/

RUN npm config set strict-ssl false
RUN npm install
RUN ./node_modules/bower/bin/bower install --allow-root

COPY . /app
RUN npm run build

CMD ["npm","start"]
