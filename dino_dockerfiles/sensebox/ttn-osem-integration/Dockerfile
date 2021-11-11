FROM node:6-alpine

ENV NODE_ENV=production

# taken from node:6-onbuild
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
COPY yarn.lock /usr/src/app/

# npm rebuild is required because the prebuilt binaries are not compatible with musl
# remove when https://github.com/kelektiv/node.bcrypt.js/issues/528 is resolved
RUN apk --no-cache --virtual .build add build-base python git \
 && yarn install --pure-lockfile --production \
 && npm rebuild bcrypt --build-from-source \
 && apk del .build
COPY . /usr/src/app

CMD [ "npm", "start" ]
