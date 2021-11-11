# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing permissions and limitations under the
# License.

# FROM node:16.1.0-alpine AS base

FROM alpine:3.13.5 AS base

RUN apk update && apk upgrade && apk add --update --no-cache nodejs npm tini

WORKDIR /root/nest-app

# RUN npm i -g npm

RUN npm install -g yarn

COPY . .

ENTRYPOINT [ "/sbin/tini", "--" ]


FROM base AS builder

RUN yarn

RUN yarn build:common

RUN yarn build:back


FROM base as release

ARG ARG_MONGODB_USER
ARG ARG_MONGODB_PASSWORD
ARG ARG_MONGODB_URL
ARG ARG_MONGODB_CLUSTER
ARG ARG_MONGODB_DB
ARG ARG_REACT_APP_AUTH0_DOMAIN
ARG ARG_REACT_APP_AUTH0_CLIENT_ID
ARG ARG_NODE_ENV

ENV MONGODB_USER=${ARG_MONGODB_USER}
ENV MONGODB_PASSWORD=${ARG_MONGODB_PASSWORD}
ENV MONGODB_URL=${ARG_MONGODB_URL}
ENV MONGODB_CLUSTER=${ARG_MONGODB_CLUSTER}
ENV MONGODB_DB=${ARG_MONGODB_DB}
ENV REACT_APP_AUTH0_DOMAIN=${ARG_REACT_APP_AUTH0_CLIENT_ID}
ENV REACT_APP_AUTH0_CLIENT_ID=${ARG_REACT_APP_AUTH0_DOMAIN}
ENV NODE_ENV=${ARG_NODE_ENV}

COPY --from=builder . /root/nest-app

EXPOSE 3010

RUN cd packages/backend

CMD cd /root/nest-app/packages/backend && yarn start
