FROM node:7.8.0

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY package.json /opt/app/
RUN npm install

COPY . /opt/app

WORKDIR /opt/app

EXPOSE 80

CMD node /opt/app/index.js