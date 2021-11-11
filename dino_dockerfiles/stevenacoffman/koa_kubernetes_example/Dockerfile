# if you're doing anything beyond your local machine, please pin this to a specific version at https://hub.docker.com/_/node/
FROM node:8.6-alpine

# tini and su-exec because both PID 1 and root are special
# --no-cache option preferred over --update
RUN apk add --no-cache su-exec tini

# WORKDIR Will create directory if it doesn't exist,
# dependencies in a different location from source for easier app bind mounting for local development
WORKDIR /opt

# Install dependencies first, add code later: docker is caching by layers
COPY package.json /opt

# Wildcard to optionally copy if present for private npm registry
# COPY .npmrc* /opt
# For npm@5 or later, copy package-lock.json as well
COPY package.json package-lock.json ./

# Docker base image is already NODE_ENV=production
RUN npm install && npm cache clean --force
ENV PATH /opt/node_modules/.bin:$PATH
# Avoid leaking credentials to private npm registries
RUN rm -f .npmrc*

# copy in our source code last, as it changes the most
WORKDIR /opt/app
COPY . /opt/app

# Arguments may change independent of source code, order after


ARG GIT_REPO="unknown"
ARG GIT_COMMIT="unknown"
ARG GIT_BRANCH="unknown"
ARG BUILD_TIME="unknown"

LABEL name="Koa Kubernetes Example" \
  maintainer="StevenACoffman" \
  git-repo="$GIT_REPO" \
  git-commit="$GIT_COMMIT" \
  git-branch="$GIT_BRANCH" \
  version="$GIT_COMMIT" \
  build_time="$BUILD_TIME" \
  description="Example Flask app with Prometheus for Kubernetes"

# set our node environment, either development or production
# defaults to production, compose overrides this to development on build and run
ARG NODE_ENV=production
ENV NODE_ENV $NODE_ENV

# default to port 8888 for node, and 5858 or 9229 for debug
ARG PORT=8888
ENV PORT $PORT
EXPOSE $PORT 5858 9229

# if you want to use npm start instead, then use `docker run --init in production`
# so that signals are passed properly. Note the code in app.js is needed to catch Docker signals
# using node here is still more graceful stopping then npm with --init afaik
# Perhaps mitigated by tini?

# Set tini as the default entrypoint
ENTRYPOINT ["tini", "--"]

CMD [ "node", "app.js" ]
