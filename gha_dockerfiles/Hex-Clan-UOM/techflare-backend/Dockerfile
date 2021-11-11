FROM node:lts-alpine3.14

WORKDIR /usr/src/app

COPY ./package.json ./
COPY ./package-lock.json ./

RUN npm install --global nodemon
RUN npm install --only=prod && npm cache clean --force

COPY . .

EXPOSE 5000

CMD [ "npm", "run", "dev" ]