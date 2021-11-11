FROM node:5-slim

WORKDIR /usr/src/app

RUN mkdir -p /usr/src/app
COPY app.js /usr/src/app/app.js

EXPOSE  80

CMD [ "node", "app.js" ]