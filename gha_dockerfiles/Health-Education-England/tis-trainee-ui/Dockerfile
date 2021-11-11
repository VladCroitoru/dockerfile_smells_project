FROM node:12.4.0-alpine

RUN mkdir /app

COPY . /app

WORKDIR /app

ENV PATH="/app/node_modules/.bin:${PATH}"

RUN npm install --production

RUN npm run prebuild

RUN npm run build

RUN npm install -g serve

CMD serve -p 3000 -s build