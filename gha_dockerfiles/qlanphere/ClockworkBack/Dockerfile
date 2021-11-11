FROM node:12.18.4

WORKDIR /code

COPY package*.json ./api
RUN npm install

COPY .  .

EXPOSE 3000
CMD [ "nodemon", "index.js" ]