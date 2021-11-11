# syntax = docker/dockerfile:1

ARG NODE_VERSION=set-node-version-as-build-arg

FROM node:$NODE_VERSION     AS node
FROM nginx:stable-alpine    AS nginx
FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:0-$NODE_VERSION AS devnode

#############################
FROM devnode AS development

ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG USERNAME=node

RUN if [ "$USER_GID" != "1000" ] || [ "$USER_UID" != "1000" ]; then \
  groupmod --gid $USER_GID $USERNAME \
  && usermod --uid $USER_UID --gid $USER_GID $USERNAME \
  && chown -R $USER_UID:$USER_GID /home/$USERNAME; \
  fi

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
  && apt-get -y install --no-install-recommends \
  less \
  tree \
  # #
  # # Clean up
  # && apt-get autoremove -y \
  # && apt-get clean -y \
  # && rm -rf /var/lib/apt/lists/* \
  && true
ENV DEBIAN_FRONTEND=dialog

USER $USER_UID

#############################
FROM node AS files
WORKDIR /x
RUN \
  apt-get update -y && \
  apt-get install --no-install-recommends -y rsync && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*
RUN --mount=type=bind,target=/s \
  rsync --archive --inplace --exclude=nginx.conf \
  /s/ /x/

#############################
FROM node AS buildenv

ARG CI=true
ARG SITE_COMMIT
ARG SITE_VERSION
ENV CI ${CI}
ENV SITE_COMMIT ${SITE_COMMIT}
ENV SITE_VERSION ${SITE_VERSION}
ENV GATSBY_TELEMETRY_DISABLED=1
ENV CYPRESS_CACHE_FOLDER /workdir/.cache/Cypress

RUN mkdir /workdir
WORKDIR /workdir

COPY --from=files /x/package.json /x/yarn.lock ./
RUN yarn install --frozen-lockfile
COPY --from=files /x/ ./

###################
FROM buildenv AS setup
RUN yarn run setup

###################
FROM setup AS lint
RUN yarn run lint

###################
FROM setup AS build
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN yarn run build --verbose

###################
FROM node AS compress
RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache
RUN \
  apt-get update && \
  apt-get install --no-install-recommends -y pigz && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*
RUN mkdir /workdir
WORKDIR /workdir

COPY package.json ./
COPY script/ ./script/
COPY --from=build /workdir/public/ ./public/

RUN yarn run compress

#################################
FROM nginx AS final

LABEL Maintainer="Christian Höltje <https://docwhat.org>"
LABEL Name="Website for docwhat.org"
LABEL org.opencontainers.image.authors="Christian Höltje <https://docwhat.org>"
LABEL org.opencontainers.image.title="Website for docwhat.org"
LABEL org.opencontainers.image.url="https://docwhat.org/"

HEALTHCHECK --interval=5s --timeout=5s CMD wget http://localhost/nginx-health -q -O - > /dev/null 2>&1

COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=lint /workdir/package.json /etc/docwhat.json
COPY --from=compress /workdir/public/ /html/
