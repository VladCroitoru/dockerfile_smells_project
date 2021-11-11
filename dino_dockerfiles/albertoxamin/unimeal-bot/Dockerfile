FROM node:10-slim
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm i
COPY . .
CMD [ "npm", "start" ]
