FROM node:lts

WORKDIR /prueba-rest-api
COPY ./package*.json ./
RUN npm install
COPY . .

EXPOSE 3000
CMD npm start