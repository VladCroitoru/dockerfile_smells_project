FROM node:alpine as build-stage
WORKDIR /docusaurus

COPY package*.json ./
RUN yarn install

COPY . /docusaurus
RUN yarn build

FROM caddy:latest as production-stage

COPY --from=build-stage /docusaurus/build /srv
COPY Caddyfile /etc/caddy/Caddyfile

EXPOSE 80
