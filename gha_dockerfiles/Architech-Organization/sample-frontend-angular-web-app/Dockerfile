FROM node:14.18-slim

RUN mkdir /server
WORKDIR /server

RUN npm install http-server -g

COPY ./dist .

EXPOSE 8080

CMD ["http-server"]



