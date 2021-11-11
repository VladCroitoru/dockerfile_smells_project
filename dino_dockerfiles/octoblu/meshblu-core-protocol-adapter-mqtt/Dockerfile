FROM octoblu/node:7-alpine-gyp

EXPOSE 1883

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG NPM_TOKEN
RUN if [ -n "${NPM_TOKEN}" ]; then echo '//registry.npmjs.org/:_authToken=${NPM_TOKEN}' > .npmrc; fi
COPY package.json yarn.lock /usr/src/app/
RUN yarn --no-progress --no-emoji --production && yarn cache clean
COPY . /usr/src/app

CMD [ "node", "--max-executable-size=256", "--max-old-space-size=256", "--max-semi-space-size=2", "command.js" ]
