FROM node:10-alpine as build-step


RUN mkdir -p /app

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . /app

EXPOSE 4200
EXPOSE 3000
EXPOSE 80
EXPOSE 443

RUN npm run build --prod

#stage 2

FROM nginx:1.17.1-alpine

COPY --from=build-step /app/docs /usr/share/nginx/html
