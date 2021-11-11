FROM node:alpine AS base

RUN apk update
RUN apk upgrade
RUN apk add bash g++ make python3 git

ARG GIT_VERSION=0
LABEL vcs-ref=$GIT_VERSION

WORKDIR /usr/src/batch-explorer

COPY package*.json ./

RUN npm install

ARG HERMEZ_API_URL

ENV REACT_APP_HERMEZ_API_URL=${HERMEZ_API_URL}

COPY . .

RUN npm run build

EXPOSE 80

CMD ["npm", "run", "start:prod"]
