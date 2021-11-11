# syntax=docker/dockerfile:1.0.0-experimental

# shared for dev/prod
FROM node:14.5-alpine3.12 AS base

WORKDIR /code
COPY . .
RUN yarn

EXPOSE 7268

# development image
FROM base AS development

ENTRYPOINT ["yarn", "start"]


# build process for prod
FROM base AS build

ENV NODE_ENV=production
RUN yarn build


# production image
FROM node:14.5-alpine3.12

RUN mkdir -p /opt/project \
    && addgroup app \
    && adduser -S -D -H -h /opt/project app

WORKDIR /opt/project

COPY --from=build /code/dist /opt/project

USER app

EXPOSE 7268

ENTRYPOINT ["node"]
CMD ["index.js"]
