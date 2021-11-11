# syntax=docker/dockerfile:experimental
# Requires DOCKER_BUILDKIT=1

FROM node:14.15.4 as builder

RUN mkdir /app
WORKDIR /build

COPY package*.json ./

ENV NEXT_TELEMETRY_DISABLED 1

RUN npm ci

COPY components components
COPY data data
COPY helpers helpers
COPY layouts layouts
COPY loaders loaders
COPY models models
COPY pages pages
COPY public public
COPY scripts scripts
COPY next-env.d.ts .
COPY next.config.js .
COPY tsconfig.json .

ARG GIT_COMMIT
ENV NEXT_PUBLIC_GIT_COMMIT=$GIT_COMMIT

ARG BUILD_DATE
ENV NEXT_PUBLIC_BUILD_DATE=$BUILD_DATE

ARG WEBSITE_URL
ENV WEBSITE_URL=$WEBSITE_URL

ARG ENABLE_SITEMAP
ENV ENABLE_SITEMAP=$ENABLE_SITEMAP

ARG ANALYTICS_URL
ENV ANALYTICS_URL=$ANALYTICS_URL

ARG HCAPTCHA_SITE_KEY
ENV HCAPTCHA_SITE_KEY=$HCAPTCHA_SITE_KEY

ENV NODE_ENV production

RUN --mount=type=secret,id=GITHUB_ACCESS_TOKEN,required npm run build
RUN npm run export

FROM nginx:alpine

RUN mkdir /www
EXPOSE 80
WORKDIR /www

COPY nginx-config.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /build/out /usr/share/nginx/html
