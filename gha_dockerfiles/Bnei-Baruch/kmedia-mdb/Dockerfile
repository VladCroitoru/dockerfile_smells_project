ARG cdn_url="https://cdn.kabbalahmedia.info/"
ARG public_base="https://kabbalahmedia.info/"
ARG feed_api_url="https://kabbalahmedia.info/feed_api/"
ARG chronicles_url="https://chronicles.kli.one/"

FROM bneibaruch/kmedia_base:latest as build

LABEL maintainer="edoshor@gmail.com"

ARG cdn_url
ARG public_base
ARG feed_api_url
ARG chronicles_url

WORKDIR /app

ENV REACT_APP_ENV=production \
    REACT_APP_API_BACKEND=/backend/ \
    REACT_APP_ASSETS_BACKEND=/assets/ \
    REACT_APP_IMAGINARY_URL=/imaginary/ \
    REACT_APP_IMAGINARY_INTERNAL_HOST=nginx \
    REACT_APP_LOCALES_BACKEND=/ \
    REACT_APP_CDN_URL=${cdn_url} \
    REACT_APP_PUBLIC_BASE=${public_base} \
    REACT_APP_FEED=${feed_api_url} \
    REACT_APP_CHRONICLES_BACKEND=${chronicles_url}

COPY . .

RUN yarn install --frozen-lockfile && \
    yarn build:svgs && \
    yarn build:scripts && \
    yarn build:css && \
    rm -rf node_modules && \
    yarn install --production --frozen-lockfile

FROM node:15-slim

ARG cdn_url
ARG public_base
ARG feed_api_url
ARG chronicles_url

WORKDIR /app
COPY --from=build /app .

ENV NODE_ENV=production \
    REACT_APP_BASE_URL=${public_base} \
    REACT_APP_API_BACKEND=http://nginx/backend/ \
    REACT_APP_CMS_BACKEND=${public_base}cms/ \
    REACT_APP_ASSETS_BACKEND=${public_base}assets/ \
    REACT_APP_IMAGINARY_URL=${public_base}imaginary/ \
    REACT_APP_IMAGINARY_INTERNAL_HOST=nginx \
    REACT_APP_CDN_URL=${cdn_url} \
    REACT_APP_PUBLIC_BASE=${public_base} \
    REACT_APP_FEED=${feed_api_url} \
    REACT_APP_CHRONICLES_BACKEND=${chronicles_url}

EXPOSE 3001
ENTRYPOINT ["/app/misc/docker-entrypoint.sh"]

