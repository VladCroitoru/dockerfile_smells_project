# ---- Base image ----
FROM hmctspublic.azurecr.io/base/node:12-alpine as base
COPY package.json yarn.lock ./
COPY tsconfig.json tsconfig.prod.json ./
COPY config ./config
RUN yarn install --production \
  && yarn cache clean

# ---- Build image ----
FROM base as build
RUN yarn install
COPY gulpfile.js ./
COPY --chown=hmcts:hmcts src/main ./src/main
RUN yarn compile \
  && yarn setup

# ---- Runtime image ----
FROM base as runtime
COPY --from=build $WORKDIR/src/main ./src/main
EXPOSE 4000
CMD [ "yarn", "start-prod" ]
