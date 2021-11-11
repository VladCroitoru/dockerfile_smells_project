# Build Stage 1
# Build/Transform your code for production
# Most common case would be building typescript to javascript
#
FROM node:16-alpine AS builder
WORKDIR /usr/src/app
COPY package.json yarn.lock ./
RUN yarn install

# Copy all the files that you need for the build
# Maybe you also have some config for typescript as well
#
COPY src src
COPY types types
COPY public public
COPY firebase firebase
COPY tsconfig.json .babelrc ./

RUN yarn build

# Build Stage 2
# Take the build from the previous stage
#
FROM node:16-alpine
WORKDIR /usr/src/app

COPY package.json yarn.lock ecosystem.json .env.prod ./
RUN yarn install --production

COPY --from=builder ./usr/src/app/dist/ dist/
COPY --from=builder ./usr/src/app/public/ public/

CMD yarn pm2
