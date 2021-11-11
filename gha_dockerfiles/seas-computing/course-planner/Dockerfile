# Use a multi-stage build to handle the compiling, installing, etc.

# STAGE 1: Install node_modules on a stretch container
FROM node:14 as base
ARG APP_DIR=/node
ARG OPEN_PORT=3000
EXPOSE ${OPEN_PORT}
WORKDIR ${APP_DIR}
RUN chown node:node ${APP_DIR}
COPY --chown=node:node package*.json ./
RUN ["npm", "install", "--global", "npm"]
USER node
RUN ["npm", "ci", "--no-optional"]
COPY --chown=node:node . . 

# STAGE 2: Extend the base image as a builder image
FROM base as builder
RUN npm run build:server && rm -rf node_modules && npm ci --no-optional --production

# STAGE 3: Copy the 'build' directory from previous stage and run in alpine
# Since this does not extend the base image, we need to set workdir, user, etc. again.
FROM node:14-alpine
ARG APP_DIR=/node
ARG OPEN_PORT=3000
EXPOSE ${OPEN_PORT}
WORKDIR ${APP_DIR}
COPY --from=builder --chown=node:node $APP_DIR/tsconfig.production.json ./tsconfig.json
COPY --from=builder --chown=node:node $APP_DIR/node_modules ./node_modules
COPY --from=builder --chown=node:node $APP_DIR/build ./
USER node 
CMD ["node", "--require", "tsconfig-paths/register", "./server/index.js"]
