FROM node:8-alpine

WORKDIR /app

COPY . /app

ENV NODE_ENV=production

RUN npm install

CMD ["node", "."]