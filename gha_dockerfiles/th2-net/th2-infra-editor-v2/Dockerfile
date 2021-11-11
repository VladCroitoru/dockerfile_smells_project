FROM node:10.23 AS build
ARG app_version=0.0.0
RUN apt-get update \
    && apt-get install --yes --no-install-recommends make build-essential
WORKDIR /home/node
COPY ./ .
RUN npm run build

FROM nginx:1.17.10-alpine
ENV NGINX_PORT=8080
COPY --from=build /home/node/build /usr/share/nginx/html
