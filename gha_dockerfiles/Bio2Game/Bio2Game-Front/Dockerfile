FROM node:16.6.1
WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm build

EXPOSE 6001

CMD npm run start
