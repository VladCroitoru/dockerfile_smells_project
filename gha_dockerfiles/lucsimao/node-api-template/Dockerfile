FROM node:alpine as builder

WORKDIR /usr/app

COPY package*.json ./
RUN npm i 

COPY . . 

RUN npm run build


EXPOSE 8080

CMD ["npm", "start"]
