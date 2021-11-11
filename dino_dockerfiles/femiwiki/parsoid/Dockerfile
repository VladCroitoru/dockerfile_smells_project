FROM --platform=$TARGETPLATFORM node:10-alpine

# Environment variables used by Mathoid
ENV APP_CONFIG_PATH=/srv/parsoid/config.yaml
ENV APP_BASE_PATH=/srv/parsoid/node_modules/parsoid

#
# Healthcheck
#
RUN apk add --no-cache curl
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
    CMD curl -f http://localhost:8000/_version || exit 1

#
# Install parsoid
#
WORKDIR /srv/parsoid
RUN apk add --no-cache --virtual .build-deps \
    git make gcc g++ python
COPY package.json .
RUN yarn --frozen-lockfile

# Remove build dependencies
RUN apk del .build-deps

#
# Config
#
COPY config.yaml .
ENV NODE_ENV=production
EXPOSE 8000
CMD sed -i 's~PARSOID_NUM_WORKERS~'"${PARSOID_NUM_WORKERS:-'ncpu'}"'~' /srv/parsoid/config.yaml &&\
    sed -i 's~MEDIAWIKI_APIS_URI~'"${MEDIAWIKI_APIS_URI:-http://http/api.php}"'~' /srv/parsoid/config.yaml &&\
    sed -i 's~MEDIAWIKI_APIS_DOMAIN~'"${MEDIAWIKI_APIS_DOMAIN:-femiwiki.com}"'~' /srv/parsoid/config.yaml &&\
    sed -i 's~MEDIAWIKI_APIS_PREFIX~'"${MEDIAWIKI_APIS_PREFIX:-femiwiki}"'~' /srv/parsoid/config.yaml &&\
    sed -i 's~MEDIAWIKI_LINTING~'"${MEDIAWIKI_LINTING:-false}"'~' /srv/parsoid/config.yaml &&\
    $APP_BASE_PATH/tools/sync-baseconfig.js \
        --domain "${MEDIAWIKI_APIS_DOMAIN:-femiwiki.com}" \
        --prefix "${MEDIAWIKI_APIS_PREFIX:-femiwiki}" \
        --config /srv/parsoid/config.yaml &&\
    node $APP_BASE_PATH/bin/server.js
