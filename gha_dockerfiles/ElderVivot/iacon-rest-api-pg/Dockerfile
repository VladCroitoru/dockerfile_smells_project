FROM node:12
WORKDIR /usr/programming/iacon-rest-api-pg
COPY . .
RUN npm install --only=prod
RUN npm build
CMD npm start