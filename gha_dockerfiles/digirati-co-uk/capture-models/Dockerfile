FROM node:12 as build

WORKDIR /home/node/app

ADD ./packages/server/package.json /home/node/app/package.json
COPY ./packages/server/pin-version.sh /home/node/app/pin-version.sh

ARG PINNED_CAPTURE_MODEL_VERSION=default

RUN yarn install --no-interactive

RUN ./pin-version.sh "$PINNED_CAPTURE_MODEL_VERSION"

COPY ./packages/server/src /home/node/app/src
COPY ./packages/server/tsconfig.docker.json /home/node/app/tsconfig.json

RUN yarn build

FROM node:12 as build-prod

WORKDIR /home/node/app

ADD ./packages/server/package.json /home/node/app/package.json
COPY ./packages/server/pin-version.sh /home/node/app/pin-version.sh

ARG PINNED_CAPTURE_MODEL_VERSION=default

RUN yarn install --no-dev --no-interactive

RUN ./pin-version.sh "$PINNED_CAPTURE_MODEL_VERSION"

FROM node:12

RUN npm install -g pm2

ENV SERVER_PORT=3000
ENV DATABASE_HOST=localhost
ENV DATABASE_NAME=capture_model_api
ENV DATABASE_PORT=5400
ENV DATABASE_USER=capture_model_api
ENV DATABASE_SCHEMA=public
ENV DATABASE_PASSWORD=capture_model_api_password
ENV FIXTURE_PATH=/home/node/app/fixtures
ARG PINNED_CAPTURE_MODEL_VERSION=default

EXPOSE 3000

WORKDIR /home/node/app

COPY --from=build-prod /home/node/app/node_modules /home/node/app/node_modules
COPY --from=build /home/node/app/package.json /home/node/app/package.json
COPY --from=build /home/node/app/yarn.lock /home/node/app/yarn.lock
COPY --from=build /home/node/app/lib /home/node/app/lib
COPY ./packages/server/ecosystem.config.js /home/node/app/ecosystem.config.js
COPY ./packages/server/pin-version.sh /home/node/app/pin-version.sh
COPY ./fixtures /home/node/app/fixtures

RUN ./pin-version.sh "$PINNED_CAPTURE_MODEL_VERSION"

USER node

CMD ["pm2-runtime", "start", "./ecosystem.config.js", "--only", "server-ui-prod"]
