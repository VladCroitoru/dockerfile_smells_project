# syntax = docker/dockerfile:experimental
FROM node:17.0.1-slim AS dependencies
WORKDIR /usr/src
RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt/lists \
    apt-get -y update && \
    apt-get -y install \
        git
COPY package.json yarn.lock /usr/src/
COPY plugins/historia-feed-plugin/package.json /usr/src/plugins/historia-feed-plugin/
COPY plugins/historia-compat-plugin/package.json /usr/src/plugins/historia-compat-plugin/
COPY plugins/historia-remark-plugin/package.json /usr/src/plugins/historia-remark-plugin/
COPY plugins/historia-soarer-update-plugin/package.json /usr/src/plugins/historia-soarer-update-plugin/
COPY plugins/historia-taxonomy-plugin/package.json /usr/src/plugins/historia-taxonomy-plugin/
RUN --mount=type=tmpfs,target=/tmp \
    --mount=type=cache,target=/usr/local/share/.cache/yarn \
    yarn

FROM dependencies AS dev
RUN --mount=type=cache,target=/mnt/yarn,id=/usr/local/share/.cache/yarn \
    cp -r /mnt/yarn /usr/local/share/.cache/

FROM dependencies AS build
ARG GATSBY_UPDATE_INDEX=false
COPY . /usr/src
RUN --mount=type=tmpfs,target=/tmp \
    yarn build

FROM scratch AS cache
COPY --from=build /usr/src/.cache /usr/src/.cache
COPY --from=build /usr/src/public /usr/src/public

FROM nginx:1.21.3-alpine
COPY conf /etc/nginx/conf.d
COPY --from=build /usr/src/public /usr/share/nginx/html
