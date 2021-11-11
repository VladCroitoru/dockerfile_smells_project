FROM node:lts-alpine

RUN apk add git --no-cache 

COPY . /app

WORKDIR /app

RUN npm i && npm run build

EXPOSE 8080

CMD npm start