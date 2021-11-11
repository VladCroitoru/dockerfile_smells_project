FROM node:6

MAINTAINER Stanislav Vetlovskiy <mrerliz@gmail.com>

ENV PATH                /app/node_modules/.bin:$PATH
ENV NODE_ENV            prod
ENV URL                 'http://localhost:3000/'
ENV NAME_LENGTH         7

RUN mkdir -p /app
WORKDIR /app

COPY package.json .
RUN npm install --production --unsafe-perm
COPY . .

VOLUME ["/app", "/app/node_modules", "/app/storage"]

EXPOSE 3000

CMD npm start
