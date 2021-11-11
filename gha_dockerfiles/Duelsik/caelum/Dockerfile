FROM node:16.13

WORKDIR /code/app

COPY yarn.lock .
COPY package.json .

RUN yarn install

COPY .eslintrc.json .
COPY .prettierrc.json .

COPY tsconfig.json .

COPY .env .

# No cmd, it is just a def for docker-compose
