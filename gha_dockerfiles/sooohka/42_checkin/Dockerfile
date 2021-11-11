FROM node:14-alpine3.14

WORKDIR /home/ubuntu/app

COPY package.json .

ENV NODE_ENV=production

RUN yarn add @craco/craco
RUN yarn build

COPY . .

EXPOSE 3000

CMD [ "yarn", "serve" ]

