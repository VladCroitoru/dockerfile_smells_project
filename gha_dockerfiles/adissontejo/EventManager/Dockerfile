FROM node:lts-alpine

WORKDIR /usr/app

COPY package.json yarn.lock ./

RUN yarn

COPY . .

EXPOSE $APP_PORT

CMD [ "yarn", "dev" ]
