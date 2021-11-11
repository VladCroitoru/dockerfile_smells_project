FROM node:6.5

WORKDIR /usr/src/app

COPY package.json .

RUN npm install

COPY . .

ENTRYPOINT ["node", "index.js"]