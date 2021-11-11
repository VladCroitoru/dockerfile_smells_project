FROM node:12-alpine

WORKDIR /src
COPY package*.json ./
RUN npm install
COPY . .

CMD [ "npm", "run", "start"]