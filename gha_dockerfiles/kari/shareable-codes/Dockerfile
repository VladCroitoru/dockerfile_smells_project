FROM node:lts-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . . 

RUN npm run build

EXPOSE 9090

CMD ["npm", "run-script", "serve"]