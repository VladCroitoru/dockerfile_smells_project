FROM node:16

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

EXPOSE 80

CMD npm run start-prod
