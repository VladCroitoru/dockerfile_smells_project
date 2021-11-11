# Dockerfile for test execution environment
FROM node:16.9.0-alpine

WORKDIR /usr/src/app

ADD package.json yarn.lock /usr/src/app/
RUN yarn install --frozen-lockfile

ADD . /usr/src/app/ 
ENTRYPOINT [ "yarn", "test:coverage" ]
