# Inspired by https://github.com/kachar/yadi

# Build target base #
#####################
FROM node:14.18.0-alpine AS base

WORKDIR /app

# Default NODE_ENV to production
ARG NODE_ENV=production
ARG NEXT_PUBLIC_SITE_URL

ENV PATH=/app/node_modules/.bin:$PATH \
  NODE_ENV="$NODE_ENV" \
  NEXT_PUBLIC_SITE_URL="$NEXT_PUBLIC_SITE_URL"
ENV NEXT_TELEMETRY_DISABLED=1

COPY package.json yarn.lock /app/
COPY scripts/copy_uswds_assets.sh scripts/copy_uswds_assets.sh
EXPOSE 3000

RUN echo "Building with NODE_ENV: ${NODE_ENV}"

# Build target dependencies #
#############################
FROM base AS dependencies

# Install prod deps
RUN yarn install --production --frozen-lockfile && \
  # Cache prod dependencies
  cp -R node_modules /prod_node_modules && \
  # Install dev dependencies
  yarn install --frozen-lockfile --production=false

# Build target development #
############################
FROM dependencies AS development

COPY . /app

CMD ["yarn", "dev"]

# Build target builder #
########################
FROM base AS builder

COPY --from=dependencies /app/node_modules /app/node_modules
COPY . /app

RUN yarn lint && \
  yarn build && \
  rm -rf node_modules

# Build target production #
###########################
FROM base AS production

COPY --from=builder /app/.next /app/.next
COPY --from=builder /app/public /app/public
COPY --from=dependencies /prod_node_modules /app/node_modules

CMD ["yarn", "start"]