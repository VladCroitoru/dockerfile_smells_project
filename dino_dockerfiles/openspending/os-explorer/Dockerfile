FROM node:8.10-alpine

WORKDIR /app

RUN apk --no-cache --update add \
  autoconf \
  automake \
  build-base \
  nasm \
  libpng-dev \
  git

RUN update-ca-certificates

WORKDIR /app
ADD package.json .
RUN npm install

ADD . .
RUN npm run build

EXPOSE 8000

CMD npm start
