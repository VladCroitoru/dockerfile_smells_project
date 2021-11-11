FROM nginx:alpine

USER root

RUN apk update
RUN apk add nodejs

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

#COPY .nginx/nginx.conf /etc/nginx

RUN rm -rf /usr/share/nginx/html/*

RUN cp -r /app/dist/* /usr/share/nginx/html
