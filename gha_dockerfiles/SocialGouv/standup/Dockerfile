FROM node:14-alpine as builder

COPY . .

RUN yarn --production --frozen-lockfile --prefer-offline && yarn cache clean

ENV HASURA_URL="%%HASURA_URL%%"

RUN yarn build
RUN yarn export

FROM ghcr.io/socialgouv/docker/nginx4spa:6.47.9

COPY --from=builder /out /usr/share/nginx/html
