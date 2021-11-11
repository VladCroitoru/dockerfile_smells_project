FROM hmctspublic.azurecr.io/base/node:12-alpine as base

# ---- Build artifacts ----
# Both frontend and backend codebases are bundled from their
# .ts source into .js, producing self-sufficient scripts.
COPY --chown=hmcts:hmcts package.json yarn.lock .snyk bin ./
FROM base AS build

USER root
RUN apk update \
    && apk add  \
    bzip2=1.0.8-r1 \
    patch=2.7.6-r7 \
    fontconfig=2.13.1-r2 \
    ca-certificates \
    git \
    && rm -rf /var/lib/apt/lists/*
USER hmcts
RUN git config --global url."https://".insteadOf git://
RUN yarn install && yarn cache clean
COPY . .
RUN yarn build:ssr

# ---- Runtime image ----
FROM base AS runtime
COPY --from=build ${WORKDIR}/dist/ ./
CMD node ./server.js
