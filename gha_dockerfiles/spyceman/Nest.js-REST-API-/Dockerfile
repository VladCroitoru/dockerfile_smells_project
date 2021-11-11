FROM node:12.13-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

COPY ./dist ./dist

EXPOSE 3000

CMD ["npm", "run", "start:prod"]