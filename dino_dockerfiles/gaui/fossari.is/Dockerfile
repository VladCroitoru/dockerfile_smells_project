ARG NODE_VERSION=12.9
FROM node:${NODE_VERSION}-slim AS build

COPY . /tmp
WORKDIR /tmp

ENV NODE_ENV=production

RUN yarn --prod=false
RUN yarn run build

FROM node:${NODE_VERSION} AS runtime

COPY --from=build /tmp/dist /app
WORKDIR /app

RUN yarn global add http-server

EXPOSE 80

ENTRYPOINT ["http-server", "-p 80", "-s"]
