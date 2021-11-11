FROM node:lts-alpine

RUN mkdir -p /app 

WORKDIR /app

COPY package.json /app

RUN cd /app && npm install

COPY . /app

EXPOSE 8009

CMD npm run dev
