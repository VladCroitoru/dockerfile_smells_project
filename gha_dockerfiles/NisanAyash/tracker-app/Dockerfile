FROM node:16-alpine3.11

WORKDIR /app-tracker

COPY package.json .

RUN npm install

COPY . ./

EXPOSE 5000

CMD [ "npm", "start" ] 