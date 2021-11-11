FROM keymetrics/pm2:12-alpine
# FROM node:7.8

# RUN apt-get update && apt-get install -y build-essential python

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV

EXPOSE 4000:4000
# EXPOSE 3000:3000
# EXPOSE 5000:5000

WORKDIR /app

COPY ./package*.json ./
COPY ./server ./server
COPY pm2Server.json .

RUN npm i --production

CMD [ "pm2-runtime", "--json", "pm2Server.json"]
