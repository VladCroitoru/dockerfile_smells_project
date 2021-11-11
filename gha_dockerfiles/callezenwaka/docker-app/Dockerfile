FROM node:13-alpine

ENV MONGO_DB_USERNAME=admin \
  MONGO_DB_PWD=password

RUN mkdir -p /home/docker-app

COPY ./docker-app /home/docker-app

CMD ["node", "/home/docker-app/server.js"]