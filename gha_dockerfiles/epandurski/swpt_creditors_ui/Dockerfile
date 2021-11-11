FROM node:14.17.6-buster AS build-image

WORKDIR /usr/src/app
COPY ./ ./
RUN npm install \
  && npm run build

# This is the final app image.
FROM nginx:1.21.1-alpine AS app-image

ENV NGINX_ENVSUBST_TEMPLATE_DIR=/usr/share/nginx/html
ENV NGINX_ENVSUBST_OUTPUT_DIR=/usr/share/nginx/html

COPY --from=build-image /usr/src/app/dist /usr/share/nginx/html
COPY nginx-add-headers.conf /etc/nginx/conf.d/nginx-add-headers.conf
