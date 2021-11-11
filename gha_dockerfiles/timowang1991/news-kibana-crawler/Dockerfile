FROM node:16-alpine3.12

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run test

RUN npm prune --production

CMD ["npm", "start"]
