FROM node:alpine

LABEL maintainer="Jiayu Liu <jiayu@caicloud.io>"

WORKDIR "/opt/app/"

ADD package.json yarn.lock /opt/app/

RUN yarn

ADD . /opt/app

ENV NODE_ENV=production \
  PORT=3000 \
  PG_USER=postgres \
  PG_PASS= \
  PG_HOST=postgres \
  PG_PORT=5432 \
  PG_DBNAME=postgres \
  IMAGE_ROOT="/opt/images"

EXPOSE 3000

CMD ["node", "server.js"]
