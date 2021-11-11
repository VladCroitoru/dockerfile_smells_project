FROM node:6-alpine

WORKDIR /app

ADD . /app

RUN yarn install && \
    yarn build && \
    yarn install --production

CMD ["yarn", "start"]
