# build stage
FROM node:lts-alpine as build-stage
WORKDIR /
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
RUN node ./docker/generate-health.js

# production stage
FROM openresty/openresty:stretch as production-stage
COPY --from=build-stage /dist /usr/share/nginx/html
COPY ./docker/nginx.conf /etc/nginx/conf.d/default.conf.template

# Default configuration
ENV PORT 80
ENV SERVER_NAME _
ENV PROXY_PROTOCOL=

COPY ./docker/entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
