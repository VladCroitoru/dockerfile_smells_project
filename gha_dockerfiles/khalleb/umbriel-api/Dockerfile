FROM node:lts-alpine

WORKDIR /usr/app

COPY ./src ./src
COPY ./tmp ./tmp
COPY babel.config.js ./
COPY ormconfig.js ./
COPY package.json yarn.* tsconfig.json ./
COPY .env ./
COPY ./scripts ./
RUN yarn
RUN yarn build

ENTRYPOINT ["/usr/app/wrapper.sh"]