FROM node:13.14.0-alpine AS build-env
ADD . /app
WORKDIR /app
RUN yarn install && yarn build

FROM gcr.io/distroless/nodejs
COPY --from=build-env /app/dist /
COPY --from=build-env /app/.env /.env
CMD ["app.js"]
