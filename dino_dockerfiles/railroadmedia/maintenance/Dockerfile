FROM nginx:alpine

RUN apk update
RUN apk add nano

RUN mkdir -p /app

COPY html /app

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 99