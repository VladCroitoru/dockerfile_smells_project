FROM node:14-alpine AS BUILD_IMAGE

ARG PORT
ENV NODE_ENV "production"

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm ci

COPY . .

EXPOSE $PORT

CMD [ "npm", "start" ]
