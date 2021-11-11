FROM node:6-slim

WORKDIR /app
COPY package.json /app/package.json

RUN npm install

COPY main.js /app/main.js

CMD ["node", "main.js"]
