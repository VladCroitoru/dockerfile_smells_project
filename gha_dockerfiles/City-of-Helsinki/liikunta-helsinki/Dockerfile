# =======================================
FROM helsinkitest/node:14-slim as appbase
# =======================================

# Use non-root user
USER appuser

# Yarn
ENV YARN_VERSION 1.22.4
RUN yarn policies set-version $YARN_VERSION

# Install dependencies
COPY --chown=appuser:appuser package.json yarn.lock /app/
RUN yarn && yarn cache clean --force

# Copy all files
COPY --chown=appuser:appuser . .

# =============================
FROM appbase as development
# =============================

# Use non-root user
USER appuser

# copy all files
COPY --chown=appuser:appuser . .

# Bake package.json start command into the image
CMD ["yarn", "dev"]

# ===================================
FROM appbase as staticbuilder
# ===================================

ARG NEXT_PUBLIC_CMS_GRAPHQL_ENDPOINT
ARG NEXT_PUBLIC_UNIFIED_SEARCH_GRAPHQL_ENDPOINT
ARG NEXT_PUBLIC_NEXT_API_GRAPHQL_ENDPOINT
ARG NEXT_PUBLIC_ALLOW_UNAUTHORIZED_REQUESTS
ARG DOCKER_BUILD_ARG_NEXT_PUBLIC_DEBUG

# Use non-root user
USER appuser

# copy all files
COPY --chown=appuser:appuser . .

# Build application
RUN yarn build

# Clean all depencies...
RUN rm -rf node_modules
RUN yarn cache clean

# ... and install only production dependencies
RUN yarn install --production

# ==========================================
FROM helsinkitest/node:14-slim AS production
# ==========================================

ENV PATH $PATH:/app/node_modules/.bin

# Use non-root user
USER appuser

# Copy build, production dependencies, next configs and public files
COPY --from=staticbuilder --chown=appuser:appuser /app/.next /app/.next
COPY --from=staticbuilder --chown=appuser:appuser /app/node_modules /app/node_modules
COPY --from=staticbuilder --chown=appuser:appuser /app/next.config.js /app/next.config.js
COPY --from=staticbuilder --chown=appuser:appuser /app/public /app/public
COPY --from=staticbuilder --chown=appuser:appuser /app/i18nRoutes.config.js /app/i18nRoutes.config.js
COPY --from=staticbuilder --chown=appuser:appuser /app/next-i18next.config.js /app/next-i18next.config.js

# Expose port
EXPOSE 80

# Start ssr server
CMD ["next", "start"]
