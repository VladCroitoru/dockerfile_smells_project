# syntax=docker/dockerfile:1
FROM node:12.18.1
WORKDIR ./lipsync4urLife
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install
COPY . .
CMD npm start
