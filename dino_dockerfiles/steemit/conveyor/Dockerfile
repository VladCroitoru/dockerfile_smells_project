FROM node:10-alpine as build-stage

WORKDIR /app

# install build dependencies
RUN apk add --no-cache \
    bash \
    build-base \
    git \
    make \
    python

# install application dependencies
COPY package.json yarn.lock ./
RUN JOBS=max yarn install --non-interactive --frozen-lockfile

# copy in application source
COPY . .

# run tests and compile sources
RUN make lib ci-test

# prune modules
RUN yarn install --non-interactive --frozen-lockfile --production

# copy built application to runtime image
FROM node:10-alpine
WORKDIR /app
COPY --from=build-stage /app/config config
COPY --from=build-stage /app/lib lib
COPY --from=build-stage /app/node_modules node_modules
COPY --from=build-stage /app/user-data user-data

# setup default env
ENV PORT 8080
ENV NODE_ENV production

# app entrypoint
CMD [ "node", "lib/server.js" ]
