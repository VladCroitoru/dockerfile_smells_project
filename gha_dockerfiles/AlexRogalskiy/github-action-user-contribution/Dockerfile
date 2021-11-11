## Setting base OS layer
## docker build -t container_tag --build-arg IMAGE_SOURCE=node IMAGE_TAG=lts-alpine .
ARG IMAGE_SOURCE=node
ARG IMAGE_TAG=lts-alpine

FROM $IMAGE_SOURCE:$IMAGE_TAG

## Setting arguments
ARG VERSION="0.0.0-dev"
ARG LANG=en_US.UTF-8
ARG VCS_REF="$(date -u +\"%Y-%m-%dT%H:%M:%SZ\")"
ARG BUILD_DATE="$(git rev-parse --short HEAD)"
ARG HOME_DIR="/usr/src/app"

## Setting metadata
LABEL version=$VERSION
LABEL vcs-ref=$VCS_REF
LABEL build-date=$BUILD_DATE

LABEL name="github-action-user-contribution"
LABEL repository="https://github.com/AlexRogalskiy/github-action-user-contribution"
LABEL homepage="https://github.com/AlexRogalskiy/github-action-user-contribution"
LABEL maintainer="Nullables, Inc. <hello@nullables.io> (https://nullables.io)"

LABEL "com.github.actions.name"="GitHub action for GitHub user contribution charts"
LABEL "com.github.actions.description"="Automatically generates GitHub user contribution diagram by provided parameters"
LABEL "com.github.actions.icon"="image"
LABEL "com.github.actions.color"="yellow"

## Setting environment variables
ENV APP_DIR $HOME_DIR
ENV LC_ALL $LANG
ENV LANG $LANG

## Installing dependencies
RUN apk add --no-cache git

## Creating work directory
WORKDIR $APP_DIR

## Copying project sources
COPY dist/index.js .

COPY package*.json ./

## Installing project dependencies
RUN npm install

## Running package bundle
ENTRYPOINT [ "sh", "-c", "node $APP_DIR/index.js" ]
