# TBD? https://github.com/moby/moby/pull/31352
# ARG NODE_VERSION=latest
# FROM node:$NODE_VERSION
FROM node:latest

MAINTAINER davidkassa <david.kassa@gmail.com>

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.license="MIT" \
      org.label-schema.name="yarn-angular-cli-firebase-tools" \
      org.label-schema.description="Auto-updating Docker image based on NodeJS official image with Yarn, Angular CLI, and Firebase Tools installed." \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/davidkassa/yarn-angular-cli-firebase-tools" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

# Commands
RUN \
  apt-get update && apt-get install -y apt-transport-https \
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get update && apt-get install -y --force-yes \
     yarn \
  && yarn global add @angular/cli firebase-tools
  
