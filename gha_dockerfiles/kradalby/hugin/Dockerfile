FROM node:lts-buster as builder
WORKDIR /app

ARG HUGIN_MAPBOX_ACCESS_TOKEN
ARG HUGIN_SENTRY_DSN
ARG HUGIN_ROLLBAR_ACCESS_TOKEN

COPY package.json .
COPY yarn.lock .
RUN yarn
COPY elm.json .

COPY . .
RUN make build

FROM kradalby/nginx-ldap-auth:latest as production
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/dist /usr/share/nginx/html
