# NOTE: use the same version of travis.yml
FROM node:14-alpine

WORKDIR /app

COPY package.json /app
RUN apk --update add git && yarn --ignore-scripts && yarn cache clean

COPY . /app


CMD ["node", "."]
