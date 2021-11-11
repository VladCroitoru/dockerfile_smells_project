FROM node:16.8

# Create app directory
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm ci

COPY . . 

RUN npm run build:prod

EXPOSE 3000
CMD [ "node", "dist/index.js" ]