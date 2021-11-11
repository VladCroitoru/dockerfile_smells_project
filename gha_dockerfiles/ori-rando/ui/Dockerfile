# Stage 1
FROM node:16-alpine as build

ARG API_HOST=wotw.orirando.com
ARG API_SECURE=true

ENV API_HOST=$API_HOST
ENV API_SECURE=$API_SECURE

WORKDIR /app
COPY . /app
RUN yarn install \
 && yarn build \
 && yarn generate

# Stage 2
FROM nginx:1.19-alpine

COPY --from=build /app/dist /app
COPY ./docker/nginx/* /etc/nginx/conf.d/

WORKDIR /app

CMD nginx -g "daemon off;"

EXPOSE 80
