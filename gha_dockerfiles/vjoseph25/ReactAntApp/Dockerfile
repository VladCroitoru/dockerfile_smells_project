FROM node:14.4.0-alpine3.12

WORKDIR /app

COPY public /app/public/
COPY src /app/src/
COPY package.json /app/

RUN npm install

CMD ["npm", "start"]