FROM node:lts AS builder

COPY package.json ./
COPY yarn.lock ./
RUN yarn

COPY ./src ./src
COPY ./tsconfig.json ./
COPY ./tsconfig.build.json ./
COPY ./nest-cli.json ./

RUN yarn build

FROM node:lts-alpine

WORKDIR /usr/app

COPY --from=builder ./node_modules ./node_modules
COPY --from=builder ./dist ./dist
COPY package.json ./

EXPOSE 3000

CMD ["yarn", "start:prod"]
