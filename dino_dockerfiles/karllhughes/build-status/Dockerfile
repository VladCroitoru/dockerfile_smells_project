FROM node:8

RUN mkdir /app

WORKDIR /app

ADD ./package.json /app/package.json
ADD ./package-lock.json /app/package-lock.json

RUN npm install --silent

ADD . /app

CMD ["node_modules/.bin/nodemon", "index.js"]
