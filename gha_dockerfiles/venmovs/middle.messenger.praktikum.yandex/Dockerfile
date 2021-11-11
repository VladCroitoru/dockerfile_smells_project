FROM node:10-alpine as builder
RUN mkdir /project
WORKDIR ./project
COPY . ./project
RUN npm install
RUN npm run build

EXPOSE 3000
CMD [ "node", "server.js" ]
