FROM node:14-alpine

ENV NODE_ENV=production

WORKDIR /usr/src/app

COPY . /usr/src/app/
RUN yarn install
CMD [ "node", "/usr/src/app/src/index.js" ]