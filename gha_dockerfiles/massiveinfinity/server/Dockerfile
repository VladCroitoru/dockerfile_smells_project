FROM node:14-alpine

WORKDIR /app

COPY package.json /app/
COPY package-lock.json /app/

RUN yarn install && yarn cache clean

COPY . /app/

ENV NODE_ENV production
EXPOSE 3000

ENTRYPOINT ["node", "-r", "esm", "./bin/server", "--port", "3000"]
