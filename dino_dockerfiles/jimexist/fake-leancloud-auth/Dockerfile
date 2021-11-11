FROM node:7-alpine

LABEL maintainer Jiayu Liu <etareduce@gmail.com>

RUN addgroup -g 998 -S fake-leancloud \
    && adduser -D -u 998 -S -G fake-leancloud fake-leancloud

# grab su-exec for easy step-down from root
RUN apk add --no-cache 'su-exec>=0.2'

ENV WORKDIR /opt/fake-leancloud-auth

WORKDIR $WORKDIR

ADD package.json yarn.lock $WORKDIR/

RUN yarn

ADD . $WORKDIR/

RUN npm run build && yarn cache clean

ENV NODE_ENV=production \
    MONGO_URL=mongodb://mongo:27017/local

EXPOSE 3000

CMD ["su-exec", "fake-leancloud", "npm", "run", "start:prod"]
