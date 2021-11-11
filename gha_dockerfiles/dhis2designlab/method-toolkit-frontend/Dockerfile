FROM node:16-alpine3.11
WORKDIR /method-toolkit-frontend

COPY ./package.json ./
COPY ./yarn.lock ./

ENV PATH /method-toolkit-frontend/node_modules/.bin:$PATH

COPY . .

RUN yarn install

RUN yarn build

CMD ["yarn", "start"]