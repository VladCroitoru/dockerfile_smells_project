FROM node:alpine

RUN mkdir -p /usr/src/app

ENV PORT 3000

ARG ENV_FILE=".env.production"

WORKDIR /usr/src/app

COPY package.json /usr/src/app
COPY yarn.lock /usr/src/app

COPY . /usr/src/app
RUN rm .env.*
COPY ./docker/$ENV_FILE /usr/src/app/.env.production

# Run install before setting NODE_ENV to install all development modules
RUN yarn

ENV NODE_ENV=production

# prevent HookWebpackError: error:0308010C:digital envelope routines::unsupported with --openssl-legacy-provider
# See https://github.com/webpack/webpack/issues/14532
ENV NODE_OPTIONS='--max_old_space_size=8192 --openssl-legacy-provider'

RUN yarn build

RUN rm -Rf node_modules
RUN yarn --production

RUN yarn cache clean

EXPOSE 3000
CMD [ "yarn", "start" ]
