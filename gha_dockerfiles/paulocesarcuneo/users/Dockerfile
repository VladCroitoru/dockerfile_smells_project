FROM node:16-alpine
WORKDIR /opt/app
COPY package*.json ./
RUN yarn install
COPY . .
ENTRYPOINT yarn start
