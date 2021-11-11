FROM node:14.16.0-alpine

# app workdir
WORKDIR /app

# copy app dependencies
COPY package.json ./

# install dependecies
RUN npm --allow-root install

# build app source code
COPY . ./

RUN npm test