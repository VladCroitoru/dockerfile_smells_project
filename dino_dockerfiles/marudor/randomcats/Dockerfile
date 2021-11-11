FROM node:16-alpine as base
RUN mkdir -p /app
WORKDIR /app
COPY package.json yarn.lock .yarnrc.yml /app/
COPY .yarn /app/.yarn

FROM base as build
RUN yarn --immutable
ENV NODE_ENV=production
COPY src  /app/src/
COPY .babelrc.js /app/
RUN yarn build

FROM base as app
RUN yarn workspaces focus --production
RUN yarn dlx modclean -r -a '*.ts|*.tsx'
RUN rm -rf .yarn .yarnrc.yml
COPY --from=build /app/dist/ /app/dist/

FROM node:14-alpine
ENV NODE_ENV=production
RUN apk add --no-cache imagemagick
USER node
WORKDIR /app
COPY --from=app /app /app
CMD [ "node", "dist/index.js" ]
