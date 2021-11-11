FROM node:14-slim

RUN apt update && apt upgrade -y \
    && apt install unzip

WORKDIR /usr/src/app

COPY package*.json ./
COPY yarn.lock .

RUN yarn

COPY ./ ./

RUN yarn build

WORKDIR /tmp

ADD https://github.com/E-commerceTechnocite/e-commerce-admin-client/archive/main.zip e-commerce-admin-client.zip

RUN unzip e-commerce-admin-client.zip -d /tmp

WORKDIR ./e-commerce-admin-client-main

RUN yarn && yarn vite build --outDir=/usr/src/app/dist/admin --base=/admin

WORKDIR /usr/src/app

RUN rm -rf /tmp

EXPOSE 3000

CMD ["yarn", "start:prod"]
