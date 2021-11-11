FROM nginx:stable-alpine

RUN mkdir -p /usr/share/nginx/html/js
WORKDIR /usr/share/nginx/html

RUN apk --no-cache add curl \
  && curl -sL https://gnab.github.io/remark/downloads/remark-latest.min.js -o js/remark-latest.min.js

COPY index.html style.css ./
ONBUILD COPY . .
