##### DEVELOPMENT #####

FROM node:16-alpine3.14 as development

# set default env value to production for build process
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

RUN apk update && apk upgrade && apk --no-cache add yarn curl bash python3 g++ make libc6-compat

# if smtp server is required for app --
# RUN apk add msmtp
# RUN ln -sf /usr/bin/msmtp /usr/sbin/sendmail

# create node_modules and set ownership to non-privileged user
RUN mkdir -p /usr/src/app/node_modules
RUN chown -R node:node /usr/src/app

# non-privileged user
USER node

# @starter for consistency in production consider locking to a specific version of @nestjs/cli
RUN yarn global add @nestjs/cli

# set default app directory
WORKDIR /usr/src/app

# copy package.json and yarn lock file
COPY --chown=node:node package*.json yarn.lock ./

# install dependencies
RUN yarn install --frozen-lockfile --production=false

# copy source
COPY --chown=node:node . ./

# @starter for production consider running lint/test/etc scripts
# RUN yarn lint & yarn test

RUN yarn build

##### PRODUCTION STEP #####

FROM node:16-alpine3.14 as production

# install dumb-init to run app as PID 1 and handle signals properly
RUN apk add dumb-init

# set default env value to production
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

# create node_modules and set ownership to non-privileged user
RUN mkdir -p /usr/src/app/node_modules
RUN chown -R node:node /usr/src/app

# become non-privileged user
USER node

# set default app directory
WORKDIR /usr/src/app

# copy package.json and yarn lock file
COPY --chown=node:node package*.json yarn.lock ./

# @starter if required, copy app's complete source folder (or any specific file dependencies)
# COPY --chown=node:node . ./

# install production dependencies (`RUN npm install --only=production`)
RUN yarn install --frozen-lockfile --production

# copy dist folder
COPY --chown=node:node --from=development /usr/src/app/dist ./dist

# expose api port
EXPOSE 3000

# @starter run database migrations if required per app
# CMD ["sh", "-c", "yarn typeorm migration:run && yarn start:prod"]

CMD ["dumb-init", "node", "dist/main"]
