FROM node:16-alpine as builder

ARG NODE_ENV
ARG PUBLIC_URL

WORKDIR /assets

COPY package.json ./
RUN NODE_ENV=$NODE_ENV yarn install

COPY . ./
RUN NODE_ENV=$NODE_ENV,PUBLIC_URL=$PUBLIC_URL  yarn build

FROM nginx:alpine as production

COPY --from=builder /assets/build /usr/share/nginx/html
COPY docker-entrypoint.sh generate-config-js.sh /
RUN chmod +x docker-entrypoint.sh generate-config-js.sh

EXPOSE 80

ENTRYPOINT ["/docker-entrypoint.sh"]
