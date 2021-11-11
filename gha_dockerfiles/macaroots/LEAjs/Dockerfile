FROM node:15-alpine3.12 as base

WORKDIR /home/node/app
COPY ./app/package.json .
RUN npm install

#COPY ./app .

EXPOSE 3000
CMD [ "npm", "start" ]
