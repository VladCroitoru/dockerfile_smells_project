FROM node:14

RUN mkdir -p /usr/src/server

WORKDIR /usr/src/server
COPY package*.json ./

RUN npm install
COPY . .

EXPOSE 5000
CMD [ "npm", "run", "start:prod" ]
