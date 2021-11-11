FROM node:lts-buster-slim

WORKDIR /app

COPY ./package.json ./
COPY ./package-lock.json ./

RUN npm ci

COPY . .

RUN npm run build

EXPOSE 3030

CMD ["npm", "start"]