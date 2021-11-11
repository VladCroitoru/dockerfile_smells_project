# syntax=docker/dockerfile:experimental

# ---- Base Node ----
FROM node:16-stretch AS base
RUN npm set progress=false && \
    npm config set depth 0 && \
    npm config set ignore-scripts true
WORKDIR /data
RUN mkdir -p /home/node/.npm && \
    chown -R node:node /data && \
    chown -R node:node /home/node/.npm
COPY --chown=node:node .npmrc package.json ./

FROM base AS dependencies-update
RUN --mount=type=cache,uid=1000,gid=1000,target=/home/node/.npm \
    npm install --global --no-audit npm-check-updates && \
    ncu -u  

FROM base AS dependencies
RUN --mount=type=cache,uid=1000,gid=1000,target=/home/node/.npm \
    npm install --force --no-audit

FROM base AS publish
ARG NPM_TOKEN
ARG GIT_EMAIL
ARG GIT_USER
COPY --chown=node:node . ./
USER node
RUN git config --global user.email ${GIT_EMAIL} && \
    git config --global user.name ${GIT_USER} && \
    npm version patch -m "[skip ci] [CI] Bumping to %s" && \
    npm publish && \
    git push --tags -u origin master

# ---- Lint ----
FROM dependencies AS lint
COPY --chown=node:node . ./
CMD ["node_modules/eslint/bin/eslint.js", "."]

# ---- Test/Cover ----
FROM dependencies AS test
USER node
RUN mkdir /data/tmp/
COPY --chown=node:node wait /wait
RUN chmod +x /wait
COPY --chown=node:node . ./
CMD ["sh", "-c", "/wait && npm run coverage"]