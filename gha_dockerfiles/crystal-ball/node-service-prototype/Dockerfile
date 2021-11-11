# --- 1️⃣ Base setup ---
# Setup base image, workdir and production dependencies used in all stages

FROM node:14.17-alpine as base

# Dynamic label values should be set with env variables at build time
ARG CREATED_DATE=not-set
ARG SOURCE_COMMIT=not-set

# Labels from https://github.com/opencontainers/image-spec/blob/master/annotations.md
LABEL org.opencontainers.image.authors=hedgecock.d@gmail.com
LABEL org.opencontainers.image.created=$CREATED_DATE
LABEL org.opencontainers.image.revision=$SOURCE_COMMIT
LABEL org.opencontainers.image.title='Crystal Ball Node.js Prototype Service'
LABEL org.opencontainers.image.url=''
LABEL org.opencontainers.image.source=https://github.com/crystal-ball/node-service-prototype.git
LABEL org.opencontainers.image.licenses=ISC
LABEL com.danhedgecock.nodeversion=$NODE_VERSION

# Expose 9000 for service, 9001 for tests debugging, and 9229 for Nodemon
ARG PORT=9000
ENV PORT $PORT
EXPOSE $PORT 9001 9229

# Setting production for Node env will ensure only production dependencies are
# installed by `npm ci`
ENV NODE_ENV production

# Create service working directory with correct ownership for installs
# /opt is a linux directory convention for installed software on a machine
RUN mkdir /opt/service && chown node:node /opt/service
WORKDIR /opt/service

COPY --chown=node:node package*.json ./

# --- 2️⃣ Dependencies ---
# Stage installs the production dependencies (and native binaries needed to
# build them) Install is run as a separate stage to easily exclude build
# binaries in final production image
FROM base as deps-builder

# Install native packages needed by node-gyp to build argon
# Note this leaves behind deps, `apk del .gyp` would delete, or a build stage
# https://github.com/nodejs/docker-node/issues/282#issuecomment-356014942
RUN apk update && apk add --no-cache --virtual .gyp make gcc g++ python

# Switch to unprivileged user provided by official Node image for security best
# practices.
USER node

# Install production dependencies
RUN npm ci

# --- 3️⃣ Dev ---
# Stage installs the rest of the dev dependencies for local and testing
# workflows. Project files *are not* copied in as they're bind-mount'ed
FROM base as dev
USER node

ENV NODE_ENV=development

# Copy in production dependencies and install remaining dev deps
COPY --from=deps-builder --chown=node:node /opt/service/node_modules /opt/service/node_modules
RUN npm install

# Start the service with Nodemon!
CMD NODE_ENV=development ./node_modules/.bin/nodemon --inspect=0.0.0.0:9229 --watch src --ignore 'src/**/*.spec.js' ./src/index.js

# --- 4️⃣ Testing ---
# Run the entire test suite including linting, unit and acceptance tests for
# service as part of CI/CD using Compose
# ℹ️ Running as user node will cause code coverage copy to fail in Github actions
FROM base as tests-runner

# Tests require all resources copied in to workspace
COPY . .

# Tests require devDependencies -> pull in from dev build stage
COPY --from=dev /opt/service/node_modules /opt/service/node_modules

# Run linting and unit tests during image build to verify foundational tests
# are passing before creating prod container
RUN npm run test:lint
RUN npm run test:unit

# Testing time! Stage is used in CI to execute acceptance tests
CMD ["npm", "run", "test:acceptance"]

# --- 5️⃣ Production preparation
FROM base as pre-production
USER node

# Copy prod dependencies only (multi-stage used to exclude node-gyp native modules)
COPY --from=deps-builder --chown=node:node /opt/service/node_modules /opt/service/node_modules

# Copy files needed to run production service
COPY --chown=node:node migrations migrations
COPY --chown=node:node scripts scripts
COPY --chown=node:node src src

# --- 6️⃣ Security scanning
FROM pre-production as security-scans

# NPM audit dependencies to check for vulnerabilities (but just warn on fail b/c
# there's almost always vulnerabilities 😢)
RUN npm audit || echo "⚠️ Vulnerabilities found"

# --- 7️⃣ Production
# Default stage that will be run if you build without a target, start service
# directly with Node to ensure shutdown signals are received properly
FROM security-scans as prod

# Setup the service healthcheck calling custom check utility
HEALTHCHECK --interval=5s --timeout=1s --start-period=1s --retries=3 CMD ["node", "./scripts/healthcheck.js"] || exit 1

# 🎉 Start the service!
CMD ["node", "./src/index.js"]
