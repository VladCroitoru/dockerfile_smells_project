FROM node:latest
MAINTAINER joway wang <joway@gmail.com>
ENV NODE_ENV 'production'

RUN apt update && apt install -y nginx && apt-get autoclean
COPY ./nginx.conf /etc/nginx/sites-enabled/default

RUN mkdir -p /app
WORKDIR /app

ONBUILD COPY package.json /app/
ONBUILD RUN npm install
ONBUILD COPY . /app

ONBUILD RUN npm run build && rm -rf node_modules

EXPOSE 80
ENTRYPOINT nginx -g "daemon off;"
