FROM node:16

WORKDIR /usr/src/app

COPY package*.json ./
COPY yarn.lock ./
COPY react-single/package.json ./react-single/
COPY root-config/package.json ./root-config/


RUN yarn install --network-timeout 1000000

EXPOSE 9000
EXPOSE 8500
EXPOSE 3000

CMD ["yarn", "start"]
