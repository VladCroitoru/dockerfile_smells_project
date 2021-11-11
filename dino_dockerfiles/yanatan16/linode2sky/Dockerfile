FROM node:0.10

RUN mkdir /app
WORKDIR /app

ADD package.json /app/package.json
RUN npm install

ADD . /app

CMD [ "node", "index.js" ]