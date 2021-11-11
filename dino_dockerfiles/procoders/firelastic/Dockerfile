FROM node:6-alpine
MAINTAINER Oleg Kopachovets<ok@procoders.tech>

ARG APP_DIR=/opt/app
WORKDIR $APP_DIR

COPY package.json $APP_DIR/
RUN npm install

COPY app.js $APP_DIR/

ENV NODE_ENV=production

CMD ["node", "./app.js"]