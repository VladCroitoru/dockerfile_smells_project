FROM node:7.8-alpine

MAINTAINER ThingleMe

ENV PORT 5000
COPY . /app
RUN cd /app; npm install -d

WORKDIR /app

EXPOSE ${PORT}

CMD npm start