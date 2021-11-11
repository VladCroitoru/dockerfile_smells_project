FROM node:14.17-alpine3.14

USER root
RUN apk add --update --no-cache python3 make g++

WORKDIR /app/static-server
COPY static-server/package.json static-server/package-lock.json  ./
RUN npm ci
COPY static-server/bin ./bin/
COPY static-server/app.js ./
RUN mkdir public

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

ARG REACT_APP_UPLOAD_HOST=""
ARG REACT_APP_CHAIN_ID="31337"
ARG REACT_APP_CHAIN_NAME="Localchain"
ARG REACT_APP_CHAIN_HOST="http://localhost:8545"
ARG REACT_APP_TORUS_BUILD_ENV="testing"

COPY src src/
COPY scripts/build.js ./scripts/
COPY config ./config/
COPY public ./public/
COPY tsconfig.json tsconfig.json
EXPOSE 8080

RUN mkdir build

RUN npm run build
RUN cp -r build ./static-server/build/

WORKDIR /app/static-server

ENTRYPOINT ["node", "bin/www"]
