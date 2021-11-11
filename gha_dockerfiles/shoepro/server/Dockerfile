# Common build stage
FROM node:14.17.5-alpine3.14 as common-build-stage

RUN apk --no-cache add --virtual builds-deps build-base python3

COPY . ./shoepro-server

WORKDIR /shoepro-server

RUN npm install

RUN npm install -g pm2

EXPOSE 5000

# Production build stage
FROM common-build-stage as production-build-stage

ENV NODE_ENV production

CMD ["pm2-runtime", "start", "ecosystem.config.js"]