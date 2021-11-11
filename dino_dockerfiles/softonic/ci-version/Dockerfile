FROM node:15.11-alpine3.13

WORKDIR /usr/src/app

RUN apk add --no-cache git

COPY package.json yarn.lock ./

RUN yarn && yarn cache clean

COPY . .

ENTRYPOINT ["node", "/usr/src/app/bin/ci-version.js", "-r", "/repo"]
