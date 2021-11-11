FROM node:14-alpine as builder

COPY . .

RUN yarn --production --frozen-lockfile --prefer-offline && yarn cache clean

ENV NEXT_PUBLIC_MATOMO_SITE_ID="34"
ENV NEXT_PUBLIC_MATOMO_URL="https://matomo.fabrique.social.gouv.fr/"

RUN yarn build
RUN yarn export

FROM ghcr.io/socialgouv/docker/nginx:6.52.0

COPY --from=builder /out /usr/share/nginx/html
