ARG node_version=14.15.4-alpine3.12

# Base Docker image for multi-stage build
FROM node:${node_version} AS base

WORKDIR /usr/app

COPY next.config.js package.json package-lock.json tsconfig.json src public ./

# Builds NextJS application
FROM base AS build

RUN CYPRESS_INSTALL_BINARY=0 npm ci && npm run build

# Installs production dependencies
FROM base AS production-deps

RUN npm ci --production

# NextJS production application
FROM node:${node_version} AS nextjs-app

ENV NODE_ENV=production

WORKDIR /usr/app

COPY --from=build /usr/app/.next ./.next
COPY --from=production-deps /usr/app/node_modules ./node_modules
COPY public ./public
COPY package.json ./
COPY next.config.js ./

USER node

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD curl --fail http://localhost:80/api/health/ || exit 1

ENTRYPOINT [ "npm", "start" ]