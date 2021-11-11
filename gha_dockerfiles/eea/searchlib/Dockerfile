FROM node:14-stretch-slim

RUN runDeps="openssl ca-certificates patch" \
 && apt-get update \
 && apt-get install -y --no-install-recommends $runDeps \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/frontend \
 && chown -R node /opt/frontend

WORKDIR /opt/frontend/

RUN npm install -g pnpm

COPY . /opt/frontend

RUN chown -R node /opt/frontend

ENV CYPRESS_INSTALL_BINARY=0

USER node

RUN pnpm i || true

RUN cd packages/searchlib && pnpm build

ENV RAZZLE_ES_INDEX=global-search
ENV RAZZLE_APP_NAME=globalsearch

RUN cd packages/searchlib-standalone && pnpm build

WORKDIR /opt/frontend/packages/searchlib-standalone

EXPOSE 3000 3001 4000 4001

CMD ["yarn", "start:prod"]
