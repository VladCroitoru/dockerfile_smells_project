FROM alpine:latest as angular-builder
RUN apk add --update nodejs npm
WORKDIR /code

COPY package-lock.json .
COPY package.json .
RUN rm -rf node_modules && \
    npm ci

COPY . .
RUN npx ng build --configuration production

FROM nginxinc/nginx-unprivileged as cafe-static

COPY --from=angular-builder /code/dist/ /www
COPY --from=angular-builder /code/src/images /www/images

EXPOSE 8080
