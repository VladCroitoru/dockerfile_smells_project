FROM node:16

WORKDIR /app

COPY package*.json ./

RUN npm install --production

COPY . .

ENTRYPOINT [ "npm", "start" ]
