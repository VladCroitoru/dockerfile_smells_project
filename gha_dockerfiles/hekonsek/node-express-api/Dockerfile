FROM node:14

WORKDIR /app
COPY app.js ./
COPY package.json ./
COPY package-lock.json ./

RUN npm install

CMD node app.js