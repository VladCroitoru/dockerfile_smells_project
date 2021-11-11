FROM node:14-alpine3.12

WORKDIR /app

ADD package.json /app/package.json

RUN npm install

ADD . /app

EXPOSE 3000

CMD ["npm", "run", "start"]
