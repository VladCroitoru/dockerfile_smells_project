###

FROM node:12-alpine AS build

COPY package*.json tsconfig.json /usr/src/app/
COPY src /usr/src/app/src/
WORKDIR /usr/src/app
RUN npm install
RUN npm run build
RUN rm -rf node_modules
RUN npm install --production

###

FROM alpine:latest

RUN apk add --no-cache nodejs

WORKDIR /usr/src/app
COPY package*.json /usr/src/app/
COPY --from=build /usr/src/app/dist/ /usr/src/app/dist/
COPY --from=build /usr/src/app/node_modules/ /usr/src/app/node_modules/

VOLUME [ "/config" ]

CMD [ "node", "dist/index.js", "/" ]
